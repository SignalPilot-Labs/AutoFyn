## imo-2026-04

**Route:** known-result retrieval. The problem is real (IMO 2026/4, proposed by Valentin Imbach, SUI). I retrieved the official-style solution and three independent community solutions. The answer and proof idea are unambiguous and all three sources agree.

### Exact characterization (quoted)

From Evan Chen's notes (web.evanchen.cc/exams/IMO-2026-notes.pdf, updated 23 July 2026, page 12):

> "The answer is that θ should be 180°/n for some integer n ≥ 2."

Equivalently: **Mulan can guarantee victory in finitely many steps iff 180°/θ is an integer** (with n ≥ 2, i.e. 0° < θ ≤ 90°). Explicitly θ ∈ {90°, 60°, 45°, 36°, 30°, 180°/7, 22.5°, 20°, …}.

All three retrieved sources state this exactly; no conflicting variants found.

### Proof idea — SUFFICIENCY (Mulan wins when θ = 180°/n)

Core lemma (all sources): **if the current triangle ever has an angle equal to kθ for an integer k ≥ 1, Mulan wins** (by induction on k: cut that angle as θ + (k−1)θ; one half already has θ, the other has (k−1)θ and induction applies).

Evan Chen's clean construction to *force* a multiple of θ from an arbitrary initial triangle:
1. First move: draw an altitude → obtain a right triangle ABC with ∠A = 90°, WLOG ∠B ≤ 45°. (If n = 2, then θ = 90° and Mulan already wins.)
2. For n ≥ 3: pick the integer k with 45° < kθ ≤ 90° (exists since θ = 180°/n ≤ 60° and n ≥ 3).
3. Choose D on segment BC with ∠BAD = kθ − ∠B. Then ∠ADC = kθ (angle chase: ∠ADB = 180° − ∠B − ∠BAD = 180° − kθ, so ∠ADC = kθ).
4. Whichever half Shan-Yu keeps contains a multiple of θ (the half △ACD has ∠ADC = kθ; the other half △ABD has ∠ADB = 180° − kθ = (n−k)θ, also a multiple of θ — **this is the only place θ = 180°/n is used**). Apply the core lemma.

The deedy write-up gives an equivalent but more general "round-up" strategy: for each unmarked angle x define d(x) = (⌊x/θ⌋+1)θ − x ∈ (0,θ); a pairing claim finds two angles u,v with d(u) < v; cut so that one half contains u+d(u)=kθ and the other contains 180°−u−d(u) = (n−k)θ. Both halves marked. Win in ≤ n−1 moves.

### Proof idea — NECESSITY (Shan-Yu avoids forever when θ ≠ 180°/n)

Define an angle **safe** if it is NOT an integer multiple of θ; **unsafe** otherwise. Note θ ≠ 180°/n ⟹ 180° is itself safe (not a multiple of θ).

Key lemma (Evan Chen, the cleanest framing): **if θ ≠ 180°/n, a safe triangle cannot be divided into two unsafe triangles.** Proof: triangle ABC safe, cut from A to D on BC producing △ABD, △ACD. The four "new" angles at the cut satisfy (external-angle fact):
- ∠CDA = 180° − ∠ADB = ∠B + ∠BAD
- ∠DAC = ∠A − ∠BAD = ∠ADB − ∠C

Sum/difference of a safe angle and an unsafe angle is safe (here 180° being safe is essential). Hence if △ABD is unsafe (i.e. ∠ADB or ∠BAD is a multiple of θ), then both ∠CDA and ∠DAC are safe, so △ACD is safe. So at least one half is safe; Shan-Yu keeps it. Shan-Yu starts with any safe initial triangle (e.g. equilateral 60°×3, which is safe because 60° = kθ would force θ = 60°/k = 180°/(3k), excluded) and maintains "all angles safe" forever. Mulan never wins.

(deedy writes the same necessity as a 3-case invariant check; simoxmenblog sketches the same "four new angles / external angle" argument.)

### Credibility assessment

HIGH. Three independent sources agree on both the answer and the proof structure:
- Evan Chen's notes (web.evanchen.cc/exams/IMO-2026-notes.pdf, updated 23 July 2026, pp. 12–13) — canonical, concise, both directions. https://web.evanchen.cc/exams/IMO-2026-notes.pdf
- deedy/imo-2026 GitHub, kimi-k3 results, problem-04/current.md — full rigorous write-up + code verification (retrograde analysis on 1° and 0.5° grids returns exactly {θ : 180°/θ ∈ ℤ}; Mulan's strategy verified for all n ≤ 90; Shan-Yu's invariant survived 200×300 random cuts). Status: solved. https://raw.githubusercontent.com/deedy/imo-2026/main/results/kimi-k3/problem-04/current.md
- simoxmenblog (SIMO Retiree Blog, "IMO 2026 Day 2 Livesolve", July 19 2026) — independent human livesolve, same answer and core ideas. https://simoxmenblog.blogspot.com/2026/07/imo-2026-day-2-livesolve.html

No source disagreed. The IMO official shortlist/solutions are withheld until IMO 2027 (https://www.imo-official.com/problems/2026/), but Evan Chen's notes are his post-IMO solution writeups, the standard community reference.

### Key structural facts the builder will need

- The game depends ONLY on the angle multiset (A,B,C) with A+B+C=180°; side lengths are irrelevant.
- **Cut geometry lemma:** cutting at vertex with angle A, parameter α ∈ (0,A) achievable by continuity/IVT, produces halves {B, α, 180°−B−α} and {C, A−α, B+α}. Every α ∈ (0,A) is realizable.
- **Halving lemma:** angle kθ ⟹ Mulan wins in k−1 moves (induction on k).
- **External-angle / four-new-angles identity:** at the cut foot, the two new angles are supplementary; specifically ∠CDA = ∠B + ∠BAD and ∠DAC = ∠A − ∠BAD. This is the crux of the necessity direction.
- **Sharpness:** Mulan wins in ≤ n−1 moves (tight worst case).

### Distinct openings for the outliner

1. **Evan-Chen altitude-first route (sufficiency) + safe/unsafe dichotomy (necessity).** The canonical, shortest path. Sufficiency: altitude → right triangle → choose k with 45° < kθ ≤ 90° → cut to land kθ in one half and (n−k)θ in the other. Necessity: "safe triangle can't split into two unsafe halves" via the external-angle identities, with 180° itself safe being the key use of θ ≠ 180°/n.
2. **Round-up / pairing route (deedy) for sufficiency.** More general and constructive: define d(x) = next multiple of θ above x minus x; prove the pairing claim (two angles u,v with d(u) < v) by contradiction using d(A)+d(B)+d(C) ∈ {θ, 2θ}; cut at angle v with α = d(u). Gives an explicit ≤ n−1 move bound. Slightly heavier bookkeeping than route 1 but a different framing.
3. **Three-case invariant route (deedy) for necessity.** Case analysis on α (multiple of θ / 180°−B−α multiple / neither) showing some half always stays safe. Equivalent to route 1's dichotomy but case-driven rather than dichotomy-driven — a rival framing of the same wall.

### Candidate technique(s)

- Combinatorial game on angle multisets; invariant (safe = not a multiple of θ) maintained by the second player; induction on k for the halving lemma. External-angle identities as the algebraic engine.
- This is a "characterize the winning θ" game problem: standard pattern is to (a) guess the family from small cases / heuristics, (b) construct Mulan's strategy for the family, (c) construct Shan-Yu's invariant for the complement.

### Cheap-kill candidates

- The necessity direction is essentially a one-lemma affair (safe triangle can't split into two unsafe halves); the sufficiency direction is one altitude + one well-chosen cut. No heavy machinery needed.
- Small-case check (conjecture, not proof): θ = 90° (n=2): Mulan draws an altitude, game ends (right angle = θ). θ = 60° (n=3): from any triangle draw altitude → right triangle (A=90, B≤45); k=1 gives 60 ∈ (45,90]; cut with ∠BAD = 60−B, lands ∠ADC = 60° = θ, Mulan wins. θ = 45° (n=4): k=2 gives 90 ∈ (45,90]; cut lands ∠ADC = 90° = 2θ, then halving lemma → θ. All consistent with the retrieved answer.

### Knowledge-base entries to use

Read `knowledge_base.md` for exact entries, but candidates by name: any "invariant / monovariant" entry (Shan-Yu's safe-angle invariant); any "combinatorial game, winning strategy characterization" entry; any "cevian / angle chasing" entry (cut geometry lemma). The external-angle fact (an exterior angle of a triangle equals the sum of the two opposite interior angles) is elementary Euclidean geometry.

### Analogous past problems (cruxes)

Retrieve from the crux corpus filtered by domain=combinatorics, subtopic ≈ "game / invariant / strategy". The simoxmenblog author draws the analogy to SMO Open 2023/5 (Jeck) and SMO Open 2019/3 (robot problem) — both "characterize the winning parameter" games with a maintained invariant — but these are NOT in the 2026 corpus and may not be in our crux corpus. Recommend the outliner search the crux corpus for "winning parameter characterization" + "second-player invariant" combinatorics problems and judge analogy individually. No forced match from me.

### Prior progress

None in `results/imo-2026-04/` was read this round (this explorer ran the known-result retrieval route only). The retrieved deedy/imo-2026 workspace marks the problem **solved** with full proof and code verification — but that is an EXTERNAL repo, not ours; our `results/` population starts fresh this round. The outliner should treat the retrieved solution as a target/verifier, not as an already-built approach.

### Dead ends (do not retry)

From deedy's "Approaches tried":
- Naive Shan-Yu invariant "all angles < θ" — works only for θ > 90°, fails generally. Don't use.
- Bare invariant "no angle equal to θ" (without the full "no multiple of θ" version) — not maintainable; Mulan can put θ in one half and nothing forbids the other. Use the stronger "no angle is an integer multiple of θ" invariant instead.

### Small-case / intuition notes (labeled as conjecture / verified-by-retrieval)

- Answer family {180°/n : n ≥ 2} verified by code retrograde analysis on 1° and 0.5° grids (deedy) — returns exactly this set. Treated as VERIFIED-against-known-result (the retrieved solution is correct), but in our run this is a target, not yet our own proof.
- Worst-case move count n−1 is tight (deedy code).
- The necessity direction's algebraic core is the external-angle identity; the necessity direction's logical core is "180° is safe" (i.e. θ ∤ 180°), which is exactly the complement of the sufficiency family.
