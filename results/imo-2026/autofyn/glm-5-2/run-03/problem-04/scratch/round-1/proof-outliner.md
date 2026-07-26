## imo-2026-04

Target (full claim, every approach): **Mulan can guarantee victory in finitely many steps ⟺ θ = 180°/n for some integer n ≥ 2** (equivalently 180°/θ ∈ ℤ). Each approach must prove BOTH directions: sufficiency (Mulan winning strategy for θ = 180°/n) and necessity (Shan-Yu counter-strategy for θ ≠ 180°/n), and state the characterization explicitly.

Game reformulation used by all (cheap reduction, proven): the state of play is fully captured by the **angle multiset** (a,b,c) with a+b+c = 180°, a,b,c > 0; side lengths are irrelevant. A cut at the vertex with angle a, parameter α ∈ (0,a) (every such α realizable by IVT on the opposite side), produces children C1 = (α, b, 180°−b−α) and C2 = (a−α, c, b+α). Shan-Yu keeps one; the other is discarded. Mulan wins iff some angle in the current triple equals θ.

---

### lattice-coset-descent: new
Target: full characterization (both directions), with the lattice L_θ = {triples having some angle ∈ θ·ℤ} as the single load-bearing object.
Technique: invariant (closedness of the complement of L_θ under Shan-Yu's defense) for necessity; explicit descent on the "multiple index" k for sufficiency. Pigeonhole-on-four-cosets is the algebraic engine.
Framing (one sentence): the answer is the set of θ for which the "contains a multiple of θ" set L_θ is a *winning attractor* — closedness of its complement (necessity) is a four-way coset intersection emptiness, and membership is reachable in one cut + a k-descent (sufficiency).
Skeleton:
  1. **Reduction to angle game.** State = angle multiset (a,b,c), a+b+c=180°. Cut geometry lemma: cut at vertex a with parameter α ∈ (0,a) gives children (α,b,180°−b−α) and (a−α,c,b+α); every α ∈ (0,a) realizable. — by IVT/elementary Euclidean geometry.
  2. **Define L_θ and the "safe" complement.** L_θ = {(a,b,c) : some angle ∈ θ·ℤ (positive multiple of θ)}; "safe" = not in L_θ (no angle is a positive multiple of θ). Note: θ itself ∈ θ·ℤ, so a winning state (some angle = θ) lies in L_θ.
  3. **NECESSITY — four-coset intersection lemma.** Let s = (a,b,c) be safe (a,b,c ∉ θ·ℤ). For a cut at vertex a with parameter x, examine when BOTH children land in L_θ:
       - C1 ∈ L_θ ⟺ [x ∈ θℤ] ∨ [180−b−x ∈ θℤ] ⟺ x ∈ θℤ ∪ (a+c − θℤ).
       - C2 ∈ L_θ ⟺ [a−x ∈ θℤ] ∨ [b+x ∈ θℤ] ⟺ x ∈ (a − θℤ) ∪ (−b + θℤ).
     The four pairwise intersections are: (i) θℤ ∩ (a−θℤ) → forces a∈θℤ ✗; (ii) θℤ ∩ (−b+θℤ) → forces b∈θℤ ✗; (iii) (a+c−θℤ) ∩ (a−θℤ) → forces c∈θℤ ✗; (iv) (a+c−θℤ) ∩ (−b+θℤ) → forces a+b+c = 180 ∈ θℤ, i.e. θ = 180/n.
     Hence **if θ ≠ 180/n, no x makes both children safe→L_θ-broken**: every cut from a safe state leaves at least one safe child. — by coset arithmetic / modular reasoning.
  4. **NECESSITY — Shan-Yu's strategy.** For θ ≠ 180/n, 180° ∉ θℤ, so θ ∤ 60 (else θ | 180); hence the equilateral (60,60,60) is safe. Shan-Yu opens equilateral; by step 3, after every Mulan cut at least one child is safe, and Shan-Yu keeps a safe child. Induct: state stays safe forever ⟹ no angle ever equals θ ⟹ Mulan never wins.
  5. **SUFFICIENCY — Phase 1 (enter L_θ in one move).** Let θ = 180/n, n ≥ 2, and let s = (a,b,c) be any state with no angle = θ (else done). WLOG (by permuting) let A = max(a,b,c), and let b',c' be the other two with c' = min. Cut at vertex A with parameter x = A + c' − kθ, where k is chosen so that kθ ∈ (c', A+c') strictly.
       - **Lattice-point lemma:** such a k (1 ≤ k ≤ n−1) exists because the open interval (c', A+c') has length A ≥ θ (n≥3 ⟹ θ ≤ 60 ≤ A; n=2 ⟹ θ=90 and the pigeonhole on the 180° sum gives A ≥ 90 with equality already θ-present; the strictly-greater case A>θ lets an open interval of length > θ straddle a lattice point of the θ-spaced lattice).
     Then C1's third angle = 180−b'−x = 180−b'−(A+c'−kθ) = kθ ∈ L_θ; C2's third angle = b'+x = b'+A+c'−kθ = 180−kθ = (n−k)θ ∈ L_θ. **Both children in L_θ regardless of Shan-Yu's discard.**
  6. **SUFFICIENCY — Phase 2 (descent on the multiple index).** State now has an angle = kθ, 1 ≤ k ≤ n−1. If k=1, θ present, done. If k ≥ 2, Mulan cuts at that vertex with x = θ (valid: 0 < θ < kθ). Children: C1 = (θ, *, *) (contains θ — Mulan wins if kept); C2 = ((k−1)θ, *, *) (contains (k−1)θ). Shan-Yu must keep C2 to avoid immediate loss; the multiple index drops k → k−1. After at most k−1 ≤ n−2 descents the index reaches 1 ⟹ θ appears. Total move bound ≤ 1 + (n−2) = n−1.
  7. **Conclusion.** Both directions established; characterization stated. Sharpness note: n−1 move bound is tight (can be checked against θ = 90 (n=2): 1 move; θ = 60 (n=3): 2 moves).
Key lemmas (claim + one-line mechanism):
  - **Four-coset intersection emptiness** — because the four ways to make both children land in L_θ each force one of {a,b,c,180} ∈ θℤ, and the safe hypothesis forbids the first three while θ ≠ 180/n forbids the fourth.
  - **Lattice-point-in-open-interval** — because an open interval of length strictly greater than θ must contain a point of the θ-spaced lattice (θ,2θ,3θ,…); the bound A ≥ θ comes from pigeonhole on a+b+c=180°.
  - **Forced k-descent** — because cutting at the kθ-vertex with x = θ makes one child contain θ (immediate win if kept) so Shan-Yu is forced to keep the (k−1)θ child, strictly decreasing k.
Open gaps:
  - Step 3: full verification that the four intersections cover all cases (the coset union is exhaustive — both children in L_θ ⟹ x lies in one of the four pairwise intersections; builder must write this cleanly).
  - Step 5 lattice-point lemma: the edge case n=2 (θ=90) needs the pigeonhole "at most one angle ≥ 90°" handled separately; the n≥3 case needs the strict inequality kθ ∈ (c',A+c') open (not just closed) to keep x ∈ (0,A).
  - Step 6: the carried angles (b,c) evolve as (b+θ,c) during descent; builder must verify they stay positive and the resulting triples remain valid (b + (k−1)θ ≤ 180 − θ − c < 180 gives boundedness; positivity is the subtle point).
Cases to cover: n=2 (θ=90, special); n≥3 (θ ≤ 60, general lattice argument); the case A = θ already-won (trivial); the case where the initial state already contains θ (0 moves).
Watch out for:
  - The four-coset lemma silently assumes a,b,c ∉ θℤ (safe); the builder must not apply it to states already in L_θ.
  - "Multiple of θ" means POSITIVE multiple (θ,2θ,…); 0 is not an angle. Keep this consistent or the coset arithmetic slips.
  - The n=2 case is degenerate (no k with 1 ≤ k ≤ n−1 = 1 except k=1, i.e. θ itself); Phase 1 must handle "already θ present" before invoking the lattice lemma.
  - Positivity of b+θ, etc. during descent — easy to assert, needs a one-line check.

---

### altitude-halving: new
Target: full characterization (both directions), sufficiency via the Evan Chen altitude construction + halving induction; necessity via the safe/unsafe external-angle dichotomy.
Technique: structural induction (halving lemma on k); constructive altitude-based cut to force a multiple of θ; external-angle identities (∠CDA = ∠B + ∠BAD) for necessity.
Framing (one sentence): the halving lemma turns "produce an angle = kθ" into a win, the altitude produces a right triangle from which one well-chosen cut (a "round k up to ≤ 90°") lands a multiple of θ in BOTH supplementary children, and the external-angle identities show a safe triangle cannot split into two unsafe halves.
Skeleton:
  1. **Reduction to angle game** (same cut-geometry lemma as above).
  2. **Halving lemma (sufficiency core).** If a triangle has an angle equal to kθ for an integer k ≥ 1, Mulan wins in ≤ k−1 moves. Proof by strong induction on k: cut that angle as θ + (k−1)θ (parameter x = θ at the vertex with angle kθ); one child contains θ (win if kept), the other contains (k−1)θ, apply induction. Base k=1: θ present, 0 moves. — by strong induction on k.
  3. **SUFFICIENCY — force a multiple of θ via altitude.** Let θ = 180°/n.
       - n = 2 (θ = 90°): any triangle has at most one angle ≥ 90° (pigeonhole on sum 180°), so at least two angles < 90°. Mulan cuts to the vertex of the third angle, choosing x = 90° − b (b one of the two < 90° angles); both children contain 90° = θ. Win in 1 move.
       - n ≥ 3: Mulan's first move draws an altitude from a vertex, producing a right triangle △ABC with ∠A = 90°; WLOG ∠B ≤ 45° (choose the smaller of the two non-right angles). Now pick the integer k with 45° < kθ ≤ 90° (exists: θ = 180°/n ≤ 60°, so k = ⌈45°/θ⌉ + small adjustment lands in (45°,90°] — builder must verify 1 ≤ k ≤ n/2 and kθ ≤ 90° strictly). Choose D on segment BC with ∠BAD = kθ − ∠B (lies in (0,∠A) = (0,90°) since ∠B ≤ 45° < kθ ≤ 90°). Angle chase: ∠ADB = 180° − ∠B − ∠BAD = 180° − kθ = (n−k)θ; hence the supplementary ∠ADC = kθ. So child △ABD has angle (n−k)θ (a multiple of θ), child △ACD has angle kθ (a multiple of θ). **Both children contain a multiple of θ.** Apply the halving lemma to whichever Shan-Yu keeps.
  4. **Conclusion of sufficiency.** Mulan forces a multiple of θ in ≤ 1 (altitude) + 1 (k-cut) = 2 moves, then halving wins in ≤ k−1 or n−k−1 more; total ≤ n−1 moves. (Sharper than the lattice-coset bound in some cases.)
  5. **NECESSITY — safe/unsafe dichotomy.** Define "unsafe angle" = a positive multiple of θ; "safe angle" = not. A triangle is safe if all three angles are safe. For θ ≠ 180°/n, 180° is itself safe (not a multiple of θ). The equilateral (60,60,60) is safe (60° = kθ ⟹ θ = 60°/k = 180°/(3k), contradicting θ ≠ 180°/n).
  6. **NECESSITY — the external-angle closure lemma.** Cut a safe triangle △ABC at vertex A, foot D on BC, producing △ABD, △ACD. The four "new" angles (two at D, one at A in each child) satisfy the **external-angle identities**:
       - ∠CDA = 180° − ∠ADB = ∠B + ∠BAD (exterior angle of △ABD at D).
       - ∠DAC = ∠A − ∠BAD = ∠ADB − ∠C (exterior angle of △ACD at D, equivalently ∠ADB = ∠C + ∠DAC).
     **Sum/difference lemma:** the sum or difference of a safe angle and an unsafe angle is safe (because a safe ± an unsafe being unsafe would force the safe one to be a difference/sum of two multiples of θ, hence itself a multiple — contradiction). **Crucial use:** 180° is safe when θ ≠ 180°/n.
  7. **NECESSITY — Shan-Yu maintains safety.** If △ABD is unsafe (i.e. ∠ADB or ∠BAD is a multiple of θ), then by the identities ∠CDA = ∠B + ∠BAD and ∠DAC = ∠A − ∠BAD, both ∠CDA and ∠DAC are safe (safe ± unsafe = safe, with ∠B, ∠A safe as the original angles); so △ACD is safe. Symmetric if △ACD is unsafe. **At least one child is safe; Shan-Yu keeps it.** Induct from equilateral: state stays safe forever, no angle = θ, Mulan never wins.
  8. **Conclusion.** Both directions; characterization stated.
Key lemmas (claim + one-line mechanism):
  - **Halving lemma** — because cutting the kθ-vertex at x = θ makes one child contain θ (immediate win) and forces Shan-Yu to keep the (k−1)θ child.
  - **Altitude round-up** — because the integer k with 45° < kθ ≤ 90° exists (θ ≤ 60° for n ≥ 3) and makes ∠BAD = kθ − ∠B lie in (0,90°), so both supplementary angles at D are multiples of θ.
  - **Safe ± unsafe = safe** — because a difference/sum of two multiples of θ is itself a multiple, so a safe angle cannot equal an unsafe ± unsafe; the contrapositive gives the lemma. 180° safe is the load-bearing input.
Open gaps:
  - Step 3: rigorous proof that the integer k with 45° < kθ ≤ 90° exists and gives ∠BAD ∈ (0,90°) — builder must handle the boundary kθ = 90° and the strict 45° < kθ.
  - Step 6: the "sum/difference lemma" needs precise statement and proof (which of sum vs. difference applies in each of the two identities; the sign matters).
  - Step 7: full case analysis — what if BOTH children are unsafe? The argument shows this cannot happen for a safe parent (the dichotomy forces ≥1 safe child); builder must write this contradiction cleanly.
Cases to cover: n=2 (θ=90, the special 90°-trick); n≥3 (θ ≤ 60, the altitude round-up); initial triangle may already contain θ (0 moves); the case ∠B = 45° exactly (boundary of the strict 45° < kθ).
Watch out for:
  - The external-angle identity ∠CDA = ∠B + ∠BAD is the exterior angle of △ABD at D, NOT of △ABC — easy to mislabel.
  - The supplementary angles at D (∠ADB + ∠ADC = 180°) is what makes "both multiples of θ" work in sufficiency: if ∠ADB = (n−k)θ then ∠ADC = 180° − (n−k)θ = kθ (since 180° = nθ).
  - "Safe" must exclude 0 (0 is a multiple of θ but not an angle); the closure lemma uses POSITIVE multiples.
  - The altitude move itself: the first move must produce a right triangle; this uses that Mulan can choose ANY point on the perimeter, including the foot of an altitude (verify the foot lies on the opposite side, not its extension — true for an acute triangle; for an obtuse triangle the altitude from the obtuse vertex still lands on the opposite side).

---

### safe-unsafe-pairing: new
Target: full characterization (both directions), with necessity via the safe/unsafe external-angle dichotomy as the spine and sufficiency via the deedy "round-up / pairing" construction (a different sufficiency mechanism from altitude-halving).
Technique: invariant (safe = no angle is a multiple of θ) closed under Shan-Yu's defense; constructive pairing of "round-up deficits" to force a multiple of θ in both children simultaneously.
Framing (one sentence): for θ = 180°/n the three round-up deficits d(a),d(b),d(c) (distance to the next multiple of θ above) sum to θ or 2θ, so two of them are comparable and Mulan cuts at one angle with parameter equal to the other's deficit, landing a multiple of θ in both supplementary children; for θ ≠ 180°/n the external-angle identities keep a safe triangle safe forever.
Skeleton:
  1. **Reduction to angle game.**
  2. **NECESSITY — safe/unsafe dichotomy + external-angle closure** (same external-angle identities and sum/difference lemma as altitude-halving steps 5–7; this approach SHARES the necessity spine with altitude-halving — that is intentional, both routes need it — but the SUFFICIENCY is genuinely different).
  3. **SUFFICIENCY — the round-up function.** Let θ = 180°/n. For each angle x ∈ (0,180°) define d(x) = (⌊x/θ⌋ + 1)·θ − x ∈ (0, θ] — the distance from x up to the next multiple of θ (strictly in (0,θ] since x is not itself a multiple unless we've already won; if d(x)=θ then x is a multiple, win). So WLOG all three angles are not multiples of θ, giving d(a),d(b),d(c) ∈ (0,θ).
  4. **SUFFICIENCY — the deficit-sum lemma.** d(a) + d(b) + d(c) ∈ {θ, 2θ}. Reason: each x = (⌊x/θ⌋+1)θ − d(x) = m_x·θ − d(x) with m_x ∈ {1,…,n}; summing, 180° = nθ = (m_a+m_b+m_c)θ − (d(a)+d(b)+d(c)), so d(a)+d(b)+d(c) = (m_a+m_b+m_c − n)θ, a positive multiple of θ bounded by 3θ, hence ∈ {θ,2θ} (the case =3θ forces all m_x = n, i.e. all x = nθ − d(x) = 180°−d(x) > 180°−θ, impossible for three positive angles summing to 180° — builder must rule this out).
  5. **SUFFICIENCY — the pairing lemma.** Since d(a)+d(b)+d(c) ∈ {θ,2θ} and each d ∈ (0,θ), at least two of the deficits — say d(u) and d(v) with u,v distinct angles — satisfy d(u) < v (or symmetrically d(v) < u). Reason: if d(a) ≥ b, d(a) ≥ c, d(b) ≥ a, d(b) ≥ c, d(c) ≥ a, d(c) ≥ b all held, summing a suitable triple gives d(a)+d(b)+d(c) ≥ a+b+c = 180° = nθ, contradicting the deficit-sum ∈ {θ,2θ} (which is ≤ 2θ < nθ for n ≥ 3; n=2 handled separately). Builder must make this pigeonhole/comparison rigorous.
  6. **SUFFICIENCY — the cut.** Cut at the vertex with angle v, choosing x = d(u) (a positive value < v by the pairing). Children:
       - C1 = (d(u), *, 180°−*−d(u)); the third angle's relation to u+d(u) = a multiple of θ is the win condition.
       - The angle-chase: the supplementary pair at the cut foot are (180° − (the two new angles)) and the carried u + d(u) = (⌊u/θ⌋+1)θ (a multiple of θ) appears in one child; the supplementary angle 180° − (⌊u/θ⌋+1)θ = (n − ⌊u/θ⌋ − 1)·θ (a multiple of θ) appears in the other.
       - **Both children contain a multiple of θ.** Apply the halving lemma (or directly: at least one child has θ or a smaller multiple).
  7. **Halving descent** (imported from altitude-halving step 2, or re-proven): once a child has an angle = kθ, Mulan wins by k-descent. Total ≤ n−1 moves.
  8. **Conclusion.** Both directions; characterization stated.
Key lemmas (claim + one-line mechanism):
  - **Deficit-sum lemma** — because 180° = nθ = (sum of next multiples up) − (sum of deficits), forcing the deficit sum to be a positive multiple of θ bounded by 2θ.
  - **Pairing lemma** — because if every deficit d(·) were ≥ every other angle, summing would give the deficit-sum ≥ 180° = nθ, contradicting ≤ 2θ.
  - **Supplementary-multiple trick** — because u + d(u) is a multiple of θ and 180° − (that multiple) is also a multiple of θ (using 180° = nθ); the two supplementary angles at the cut foot are exactly these two multiples.
Open gaps:
  - Step 4: ruling out the deficit-sum = 3θ case rigorously (it would require all three angles near 180°, impossible).
  - Step 5: the pairing lemma is the hardest step — the clean statement "∃ distinct u,v with d(u) < v" needs a careful proof; the simple summation argument may need strengthening (it's the load-bearing sub-lemma).
  - Step 6: the angle-chase tying the cut parameter x = d(u) to BOTH children landing on multiples of θ; builder must verify which angle in which child is the multiple.
  - n=2 (θ=90) special case (deficit-sum degenerates since θ is large).
Cases to cover: n=2 (degenerate, use the 90°-trick directly); n≥3 (pairing route); all three angles already multiples of θ (0 moves); exactly one angle a multiple (use halving directly).
Watch out for:
  - d(x) ∈ (0,θ] — the endpoint θ corresponds to x being a multiple, which is the "already won" case; the pairing argument assumes strict d(x) < θ, so handle the already-won case first.
  - The pairing lemma's strict inequality d(u) < v (strict, so x = d(u) ∈ (0,v) is a legal cut parameter).
  - Sharing the necessity spine with altitude-halving is fine (it's the canonical necessity argument); the DIVERSITY is in sufficiency (round-up vs. altitude), which is genuinely different.

---

### attractor-potential: new
Target: full characterization (both directions), framed as a formal game-graph attractor computation plus a potential-function termination argument, abstracting away from any specific construction.
Technique: game-theoretic attractor (least fixed point of "states containing θ ∪ states with a move whose both successors lie in W") for the necessity obstruction and the sufficiency closure; well-founded potential (minimal multiple-index) for finite-step termination.
Framing (one sentence): define the winning set W as the least attractor and prove W = all states iff θ = 180°/n — the complement of W is nonempty (and Shan-Yu-trapped) exactly when 180° ∉ θℤ, by exhibiting the closed invariant "no angle is a positive multiple of θ"; the attractor is all-of-states when 180° ∈ θℤ by exhibiting an explicit potential (the least multiple of θ bounding some angle) that strictly decreases.
Skeleton:
  1. **Reduction to angle game.**
  2. **Game-graph formalization.** State space S = {(a,b,c) : a,b,c>0, a+b+c=180°}. Move relation: s → {C1, C2} (Mulan chooses x; Shan-Yu discards). Define the **winning attractor** W as the least set with (i) {s : θ ∈ angles(s)} ⊆ W, and (ii) s ∈ W whenever ∃ x such that BOTH children C1(s,x), C2(s,x) ∈ W. Mulan wins from s iff s ∈ W. (Standard combinatorial-game attractor / least-fixed-point definition.)
  3. **NECESSITY — exhibit a non-W state when θ ≠ 180°/n.** Let I = S \ L_θ = "safe" states (no angle a positive multiple of θ). Claim I is a **trap for Mulan** (closed under Shan-Yu's defense): for any s ∈ I and any cut x, at least one child lies in I. Proof = the four-coset intersection lemma (imported from lattice-coset-descent step 3, or re-proven). Since θ ∈ θℤ ⊆ L_θ, no state in I contains θ, so I ∩ W ⊆ I ∩ L_θ = ∅. Hence I ⊆ S \ W; W ≠ S; Mulan cannot guarantee a win. Shan-Yu opens at any state in I (e.g. equilateral, safe since θ ∤ 60).
  4. **SUFFICIENCY — W = S when θ = 180°/n.** We must show every state enters W. Exhibit the potential Φ(s) = min{k ≥ 1 : some angle of s equals kθ, or ∞ if none}. Show:
       - (a) Φ(s) = 1 ⟹ s ∈ W (base case, θ present).
       - (b) If Φ(s) = k ≥ 2 (some angle = kθ), Mulan cuts at that vertex with x = θ; one child has θ (Φ=1, in W), the other has (k−1)θ (Φ = k−1). If Shan-Yu keeps the (k−1)θ child, Φ drops to k−1. So Φ strictly decreases under forced play. By well-founded induction on k, s ∈ W. (Halving descent.)
       - (c) If Φ(s) = ∞ (no angle is a multiple of θ), Mulan plays the "enter-L_θ" cut (lattice-coset-descent step 5, or the altitude round-up, or the round-up pairing) to force BOTH children into L_θ, i.e. both children have finite Φ ≤ n−1. Whichever Shan-Yu keeps has finite Φ, then case (b) applies. So s ∈ W.
  5. **Termination bound.** The potential strictly decreases (Φ: ∞ → ≤ n−1 → k−1 → … → 1), so Mulan wins in finitely many steps; bound ≤ 1 (enter) + (n−2) (descent) = n−1, matching the constructive routes.
  6. **Conclusion.** W = S ⟺ θ = 180°/n; characterization stated.
Key lemmas (claim + one-line mechanism):
  - **I is a trap** — by the four-coset intersection lemma (a safe state cannot be cut into two unsafe children without 180° ∈ θℤ).
  - **Φ strictly decreases under forced play** — because cutting the kθ-vertex at x = θ makes one child contain θ (forcing Shan-Yu's hand) and the other contain (k−1)θ.
  - **Every state has a move to a finite-Φ child** — by the lattice/altitude/pairing construction (imported as a black-box sub-lemma; this approach's distinctive contribution is the abstract attractor framing, not a new entry-cut).
Open gaps:
  - Step 3: the four-coset lemma is imported — builder must either cite the lattice-coset-descent proof or reproduce it inline. (Mark as a dependency.)
  - Step 4(c): the "enter-L_θ" cut is imported from one of the other approaches — this approach is the abstract wrapper; the builder should pick ONE entry construction (lattice max-angle, altitude round-up, or pairing) and plug it in. Flag which.
  - Step 2: the well-definedness of the attractor (least fixed point exists) — standard but the builder should state the monotone-operator framework briefly.
Cases to cover: Φ=1 (base, θ present); Φ=k≥2 (descent); Φ=∞ (entry); the boundary n=2 (θ=90, Φ∈{1,∞} only, descent is trivial).
Watch out for:
  - This approach is the MOST abstract — it risks hand-waving the entry step by importing it. The builder must not present the imported sub-lemma as proved; either prove it inline or cite a certified lemma.
  - The potential Φ = ∞ case is the crux; if the entry construction is left as a black box, the reviewer may flag a gap. Recommend the builder certify the entry lemma as a shared lemma and import it.
  - The attractor framing is genuinely different (game-theoretic, not constructive-geometric) but the underlying sub-lemmas overlap with other routes; the DIVERSITY is in the proof-organizing principle (fixed-point attractor + well-founded potential), not in new mechanics.

---

### residue-transfer-reframe: new (a deliberate probe of whether the transfer/residue viewpoint can stand alone; high-risk, may die on the reconciliation gap — that is the intended outcome if the route is genuinely subordinate to the lattice route)
Target: full characterization (both directions), with the transfer move (subtract θ from one angle, add θ to another) as the sufficiency engine and the mod-θ residue of each angle as the invariant Mulan must break.
Technique: forced deterministic transfer (Mulan subtracts θ from an angle > θ, adds θ to another); mod-θ residue invariant; residue-breaker (the 90°-trick or bisection) to escape the residue trap. THIS IS THE EXPLORER'S ANGLE-DYNAMICS ROUTE, WITH THE RECONCILIATION GAP FLAGGED HONESTLY.
Framing (one sentence): the transfer move (cut at vertex a with x = a−θ, forcing Shan-Yu to keep the (a−θ, b, c+θ) child) realizes a Euclidean-algorithm descent on angles, preserving each angle mod θ — so sufficiency reduces to exhibiting a "residue-breaker" that creates a fresh residue-0 angle, and the central open question is whether the 90°-trick/bisection suffices as a residue-breaker for ALL n (not just n with θ | 90).
Skeleton:
  1. **Reduction to angle game.**
  2. **The transfer move (forced transition).** From state (a,b,c) with a > θ, Mulan cuts at vertex a with x = a − θ. Children: C1 = (a−θ, b, c+θ) [third angle = 180−b−(a−θ) = c+θ]; C2 = (θ, c, b+a−θ) [contains θ]. Shan-Yu must keep C1 to avoid losing. So the forced transition is (a,b,c) → (a−θ, b, c+θ): **Mulan transfers θ from angle a to angle c.** — by the cut-geometry lemma + the "θ in one child forces Shan-Yu" argument.
  3. **Residue invariant (the obstruction).** Define r(s) = (a mod θ, b mod θ, c mod θ) (modular residues). The transfer move preserves r: subtracting θ from a and adding θ to c leaves both residues unchanged. **Consequence:** if no initial angle is ≡ 0 mod θ (i.e. no angle is a multiple of θ), transfers alone can NEVER produce a multiple of θ. So sufficiency cannot rest on transfers alone — it needs a residue-breaking move.
  4. **Residue-breakers (candidate moves).**
       - (a) **The 90°-trick:** from any triangle, cut to plant a 90° angle (residue 90 mod θ) — but this only produces residue 0 if θ | 90, i.e. θ = 90/m for some m. This covers θ = 90, 45, 30, 22.5, 18, … but NOT θ = 60, 36, 180/7, etc. (where 90 mod θ ≠ 0).
       - (b) **Bisection:** from a state with angle 2θ, cut at that vertex with x = θ — both children contain θ. This is a 1-move win if Mulan can first drive an angle to 2θ. Bisection preserves residues mod θ too (2θ ≡ 0), so it doesn't break the residue invariant either — it only helps once a multiple of θ is already present.
       - (c) **The reconciliation gap (HARD STEP):** for θ = 180°/n with θ ∤ 90 (e.g. θ = 60, 36, 180/7), what move breaks the residue invariant? Candidate: combine a 90°-trick (plant 90°, residue 90 mod θ) with transfers to reduce 90 mod θ down toward 0 via a Euclidean algorithm on (90 mod θ, θ); the Euclidean algorithm terminates at gcd(90,θ) — which is θ iff θ | 90. **For θ = 180/n not dividing 90, the gcd is a proper divisor of θ, not θ itself, so the Euclidean algorithm does NOT reach residue 0.** This is the obstruction.
  5. **THE RECONCILIATION (the open crux — flag honestly).** The residue route as the explorer described it CANNOT close for θ = 180/n with θ ∤ 90 (e.g. θ = 60: 90 mod 60 = 30, gcd(90,60)=30 ≠ 60). To make this route work, the builder must EITHER:
       - (i) Find a different residue-breaker (not the 90°-trick) that produces residue 0 mod θ for ALL n; OR
       - (ii) Show the residue viewpoint can be augmented: e.g. use a "180°-trick" (plant 180° — impossible, angles < 180°) or a "kθ-trick" for a k coprime to n (which is circular: finding kθ is the goal); OR
       - (iii) **Concede** that the residue route is subordinate to the lattice route (it handles the descent within L_θ but cannot establish entry into L_θ for θ ∤ 90), and import the entry step from another approach. If so, this approach collapses into lattice-coset-descent — a recorded dead-end for the standalone residue framing.
  6. **NECESSITY via the residue invariant (if it can be made to work).** For θ ≠ 180°/n, 180° mod θ ≠ 0. The residue multiset (a mod θ, b mod θ, c mod θ) with a+b+c = 180° (≡ 180 mod θ ≠ 0) is preserved by transfers; a triangle with all three residues nonzero (e.g. equilateral when 60 mod θ ≠ 0, i.e. θ ∤ 60, i.e. θ ≠ 180/n) cannot reach a residue-0 angle by transfers alone. But Mulan has NON-transfer moves too (any x ≠ a−θ), so the residue invariant does NOT directly prove necessity — the necessity proof needs the four-coset / external-angle argument. **This is a second gap: the residue invariant is too weak to prove necessity on its own, because non-transfer cuts can change residues.**
  7. **Conclusion (conditional).** IF the reconciliation (step 5) and the necessity strengthening (step 6) are resolved, the residue-transfer route gives the full characterization. IF NOT, the route is a recorded dead-end for the standalone framing, and the lesson is: the mod-θ residue is the wrong invariant; the correct one is "angle ∈ θℤ" (membership, not residue).
Key lemmas (claim + one-line mechanism):
  - **Transfer is forced** — because cutting at the a-vertex with x = a−θ makes one child contain θ, forcing Shan-Yu's discard.
  - **Transfers preserve residues mod θ** — because subtracting/adding θ leaves each angle's residue unchanged.
  - **The 90°-trick plants residue 90 mod θ** — by pigeonhole (at most one angle ≥ 90°) and the cut x = 90−b.
  - **[GAP] The residue-breaking move for θ ∤ 90** — NO KNOWN MECHANISM; this is the open crux. The Euclidean-algorithm reduction of (90 mod θ) terminates at gcd(90,θ) ≠ θ, so it does NOT reach residue 0.
Open gaps (the honest load-bearing list):
  - Step 5: the reconciliation crux — the central open question. If the builder cannot find a residue-breaker for general n, this approach dies here (and that is the intended outcome: it probes whether the residue framing is viable standalone).
  - Step 6: the necessity direction cannot be proved by the residue invariant alone (non-transfer cuts change residues); the builder must either strengthen the invariant or import the four-coset/external-angle necessity argument (which would make this approach non-standalone).
  - Step 4(b): bisection does not break residues (2θ ≡ 0 mod θ); it only helps within L_θ.
Cases to cover: θ | 90 (90°-trick works, route closes cleanly); θ = 180/n with θ ∤ 90 (the reconciliation case); θ ≠ 180/n (necessity, weak via residue alone).
Watch out for:
  - This approach is a DELIBERATE PROBE — the explorer's "θ ≤ 90°" conjecture is refuted (a discretization artifact); the residue route inherits that defect. The builder should NOT trust any parity/residue pattern from the half-degree grid.
  - If the builder finds that the residue route cannot close for θ = 60 (the simplest θ ∤ 90 case in the winning set), record it as a dead-end and recommend the route be merged into lattice-coset-descent (which uses the correct "membership in θℤ" invariant, not residues).
  - The angle-dynamics explorer's "transfer + 90-trick + bisection" recipe is INSUFFICIENT for θ = 60: explicit check — 90 mod 60 = 30, gcd(90,60) = 30, so the Euclidean reduction of 90 lands at 30, not 60; there is no residue-0 production. The builder should verify this concretely before declaring the route dead.

---

## Field list and advance recommendation

1. **lattice-coset-descent** (new) — additive explorer's full mechanism; cleanest, both directions complete with all sub-lemmas identified. The strongest candidate.
2. **altitude-halving** (new) — Evan Chen's canonical route; halving lemma + altitude round-up for sufficiency, external-angle dichotomy for necessity. Most likely to match the official solution.
3. **safe-unsafe-pairing** (new) — necessity shared with altitude-halving, sufficiency via the deedy round-up/pairing construction (genuinely different entry mechanism).
4. **attractor-potential** (new) — abstract game-theoretic wrapper; relies on importing an entry sub-lemma, so structurally dependent on (1)/(2)/(3), but provides a different organizing principle and a clean potential-based termination argument.
5. **residue-transfer-reframe** (new, high-risk probe) — the angle-dynamics explorer's route kept honest; flagged with the reconciliation gap as the load-bearing hard step. Expected outcome: either the builder finds a residue-breaker for θ ∤ 90 (unlikely, given the gcd obstruction), or the route is recorded as a dead-end and the lesson "mod-θ residue is the wrong invariant; use θℤ-membership" is fed back.

**Diversity check:** approaches (1)–(3) share the necessity spine (four-coset / external-angle — these are two phrasings of the same lemma) but differ in sufficiency (lattice max-angle cut vs. altitude round-up vs. deficit-pairing) — three genuinely different entry constructions. Approach (4) reorganizes the whole proof as a fixed-point attractor. Approach (5) probes a genuinely different invariant (mod-θ residue) and is expected to die, feeding back the lesson that the correct invariant is membership-not-residue. This is the required framing diversity (no two approaches are the same framing with a different technique).

**Advance first:** lattice-coset-descent (approach 1) — it has the most complete sub-lemma identification and both directions close cleanly. Build it first; in parallel build altitude-halving (approach 2) as the independent cross-check (if both reach the same characterization via different sufficiency, confidence is high). Defer the attractor-potential (4) and residue-transfer (5) to round 2 once the entry lemma is certified (approach 4) and the residue route is confirmed dead (approach 5). The build set for this round: lattice-coset-descent, altitude-halving, safe-unsafe-pairing (three parallel builders, one per slug).
