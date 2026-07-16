# Approach: remainder-forcing

## Status
solved

## Approaches tried
- (round 2, outliner) new skeleton: arithmetic mod θ on the angle multiset; one-cut residue forcing for sufficiency, safety preservation for necessity — outline APPROVED by outline-reviewer with three builder notes.
- (round 2, builder) filled all gaps G0–G6 into a complete prose proof below; all three reviewer notes incorporated (m′ ≤ n − 1 stated before invoking Descent; ≡ mod θ over ℝ defined before any case split, with the residue-0 ⟹ positive-multiple remark; companion-relabeling sentence in the Cut Lemma). Four-case Safety Preservation written inline AND filed as `lemmas/safe-piece-exists.md` (proposed, awaiting certification). Algebra re-checked with exact rationals (forcing: 5 values of n × random safe triangles, 0 failures; safety preservation: 89 900 random cuts across 5 non-divisor θ including irrational-like rationals, 0 failures). **Erratum vs. outline:** the suggested θ = 40° verification triangle (50°, 80°, 50°) is UNSAFE (80° = 2·40°); replaced by (55°, 55°, 70°), which is safe. — outcome: complete proof, Status set to solved.

## Current best
Complete proof of the full characterization (both directions), written below. No open gaps. Answer: Mulan can guarantee victory in finitely many steps **iff θ = 180°/n for some integer n ≥ 2**; when she can, at most n − 1 cuts suffice.

## Full proof

**Theorem.** Let 0° < θ < 180°. Mulan can guarantee victory in finitely many steps, no matter how Shan-Yu plays, **if and only if θ = 180°/n for some integer n ≥ 2** — equivalently, iff 180/θ ∈ ℤ. (Since 0° < θ < 180° forces 180/θ > 1, the condition "180/θ ∈ ℤ" automatically gives n ≥ 2.) Moreover, when θ = 180°/n, Mulan wins within at most n − 1 cuts from any starting triangle.

Throughout, a *triangle* is a nondegenerate triangle in the Euclidean plane; we identify a position of the game with the (unordered, labelled-by-vertex) triple of its interior angles, each in (0°, 180°), summing to 180° (the Euclidean angle-sum theorem). The game protocol: at the top of each iteration the *check* happens — if the current triangle has an angle exactly θ, the game stops and Mulan wins; otherwise Mulan chooses a point P on the perimeter, distinct from the three vertices, cuts from P to the opposite vertex, and Shan-Yu keeps one of the two resulting triangles. "Mulan wins within k cuts" means: whatever Shan-Yu does, the check fires at some iteration after at most k cuts have been made.

### Step 0: Congruence mod θ, multiples, safety

We use these definitions everywhere below (in particular *before* any case split, as required).

**Definition (congruence mod θ over ℝ).** For real x, y, write x ≡ y (mod θ) iff (x − y)/θ ∈ ℤ. This is an equivalence relation and is compatible with addition and subtraction: if x ≡ x′ and y ≡ y′ then x ± y ≡ x′ ± y′ (mod θ), because integers are closed under addition and subtraction. For x ∈ ℝ its *residue* is the unique r(x) ∈ [0, θ) with x ≡ r(x) (mod θ), namely r(x) = x − θ⌊x/θ⌋.

**Definition (positive multiple).** x is a *positive multiple* of θ iff x = mθ for some integer m ≥ 1.

**Remark R1 (residue 0 ⟹ positive multiple, for positive angles).** If x > 0 and x ≡ 0 (mod θ), then x/θ ∈ ℤ and x/θ > 0, so x = mθ with m ∈ ℤ, m ≥ 1: x is a positive multiple of θ. (Positivity is essential; this is why the definition applies cleanly to triangle angles, which are all > 0.) Conversely a positive multiple obviously has residue 0. So for a triangle angle x: *x is a positive multiple of θ ⟺ x ≡ 0 (mod θ) ⟺ r(x) = 0*.

**Definition (safe).** A triangle is *safe* (for θ) if none of its three angles is a positive multiple of θ; equivalently (by R1), all three angles have nonzero residue mod θ. Note a safe triangle in particular has no angle equal to θ = 1·θ, so the check never fires on a safe triangle.

### Step 1: The Cut Lemma (closes G0)

**Cut Lemma.** Let T be a triangle with angles a, b, c at vertices A, B, C.

(1) *(Realizability.)* For every t ∈ (0, a) there is a valid Mulan move — a point P on the open side BC (so P is on the perimeter and is not a vertex), cut along segment PA — with ∠BAP = t.

(2) *(Piece formula.)* For any such P with ∠BAP = t, the cut splits T into exactly two nondegenerate triangles:
- T₁ = ABP with angle triple (b, t, a + c − t) at vertices (B, A, P), and
- T₂ = APC with angle triple (a − t, c, b + t) at vertices (A, C, P).

All six listed angles lie in (0°, 180°), each triple sums to 180°, and the two angles at P are supplementary: (a + c − t) + (b + t) = 180°.

(3) *(Relabeling remark.)* The names B, C for the two endpoints of the side containing P are labels, not choices of nature: describing the same physical move with the labels swapped (B ↔ C) replaces t by a − t and swaps the roles of the two pieces. Consequently, "cut to vertex A with *companion* B and parameter t" (meaning: the piece containing B receives the new angle t at A) is a legal Mulan move for **any** vertex A, **either** companion among the other two vertices, and **any** t ∈ (0, a): Mulan realizes it by placing P at the appropriate point of the opposite side. Conversely, *every* legal Mulan move is of this form for some labeling: P lies in the interior of exactly one side; call the opposite vertex A, the side's endpoints B and C, and set t = ∠BAP.

*Proof.* (1) Place coordinates; since T is nondegenerate, A does not lie on line BC. Parametrize P(s) = (1 − s)B + sC for s ∈ [0, 1]. Then P(s) ≠ A for all s, so
f(s) := ∠BAP(s) = arccos( ⟨P(s) − A, B − A⟩ / (|P(s) − A| · |B − A|) )
is a composition of continuous functions on [0, 1], hence continuous, with f(0) = ∠BAB = 0 and f(1) = ∠BAC = a. Given t ∈ (0, a), the Intermediate Value Theorem yields s* ∈ [0, 1] with f(s*) = t; since f(0) = 0 < t and f(1) = a > t we have s* ∈ (0, 1), i.e., P = P(s*) lies strictly between B and C. So P is on the perimeter, not a vertex, and the cut PA is a valid move with ∠BAP = t.

Before proving (2) we record an angle-additivity fact.

*Claim: if P is interior to segment BC then ∠BAP + ∠PAC = ∠BAC.* Put u = B − A, v = C − A; these are linearly independent (A, B, C not collinear), and P − A = (1 − s)u + sv with s ∈ (0, 1). Choose coordinates with A at the origin, u along the positive x-axis, and v in the open upper half-plane (possible by reflecting if needed; reflections preserve angles). Write φ(w) ∈ [0°, 360°) for the polar angle of a nonzero vector w; then φ(u) = 0 and φ(v) = ∠BAC = a ∈ (0°, 180°). The closed sector S = {ρ(cos ψ, sin ψ) : ρ ≥ 0, ψ ∈ [0, a]} is convex because a ≤ 180° (it is an intersection of two half-planes). Both u and v lie in S, so the convex combination P − A = (1 − s)u + sv lies in S, and P − A ≠ 0; hence ψ := φ(P − A) ∈ [0, a]. Moreover P − A is not a nonnegative scalar multiple of u (its v-coordinate s ≠ 0 in the basis (u, v)) nor of v (its u-coordinate 1 − s ≠ 0), so ψ ∈ (0, a). Then ∠BAP = ∠(u, P − A) = ψ and ∠PAC = ∠(P − A, v) = a − ψ, whose sum is a. ∎(Claim)

(2) The cut segment PA meets the boundary of T at exactly P and A, so it divides T into the two triangles ABP and APC; both are nondegenerate since P ≠ B, P ≠ C (P interior to BC) and A ∉ line BC. Their angles:
- In ABP: at B, since P lies on segment BC with P ≠ B, ray BP equals ray BC, so ∠ABP = ∠ABC = b. At A, ∠BAP = t by construction. At P, by the angle-sum theorem, ∠APB = 180° − b − t = a + c − t (using a + b + c = 180°).
- In APC: at C, since ray CP = ray CB, ∠ACP = ∠ACB = c. At A, by the Claim, ∠PAC = a − t. At P, since B, P, C are collinear with P between B and C, ∠APB + ∠APC = 180°, so ∠APC = 180° − (a + c − t) = b + t; consistently, (a − t) + c + (b + t) = 180°.

Ranges: t ∈ (0, a) and a − t ∈ (0, a) by choice; b, c ∈ (0°, 180°) as angles of T; and a + c − t, b + t are angles of nondegenerate triangles, hence in (0°, 180°) — directly: a + c − t > a − t > 0 and a + c − t = 180° − (b + t) < 180°, and symmetrically for b + t. Supplementarity was shown above.

(3) Swapping the labels B ↔ C swaps b ↔ c and replaces t = ∠BAP by ∠CAP = a − t (by the Claim); substituting, the triple (b, t, a + c − t) becomes (c, a − t, b + t) and vice versa — the same two physical pieces, listed in the other order. So the description "vertex A, companion B, parameter t" and the description "vertex A, companion C, parameter a − t" denote the same move, and by (1) every such description with t ∈ (0, a) is realizable by an actual position of P. The converse direction is immediate: P determines the side it is interior to, hence the labeling. ∎

From now on we describe Mulan's moves as: *cut to vertex A with companion B and parameter t ∈ (0, a)*, producing the pieces T₁ = (b, t, a + c − t) (contains companion B) and T₂ = (c, a − t, b + t) (contains the other vertex C). By the Cut Lemma this is exactly the full set of legal moves.

### Direction A: θ = 180°/n with n ∈ ℤ, n ≥ 2 ⟹ Mulan wins within n − 1 cuts

Throughout Direction A, θ = 180°/n, so **180° ≡ 0 (mod θ)** (indeed 180°/θ = n ∈ ℤ).

**Observation O1 (index bound).** Every angle x of every triangle satisfies 0 < x < 180° = nθ; hence if x is a positive multiple mθ of θ, then m ≤ n − 1. *(This is the fact, flagged by the outline-reviewer, that makes the total bound n − 1 work; we will invoke it explicitly before each use of Descent.)*

**Step 2: Descent Lemma (closes G1).** *Suppose that at the top of some iteration the current triangle T has an angle equal to mθ for some integer m ≥ 1. Then Mulan wins within m − 1 further cuts, no matter how Shan-Yu plays.*

*Proof.* Strong induction on m (KB: Proof techniques — Induction, strong).

*Base m = 1.* T has an angle equal to θ, so the check at the top of this iteration fires and Mulan wins with 0 = m − 1 further cuts.

*Inductive step m ≥ 2.* Assume the lemma for all integers m′ with 1 ≤ m′ < m. Let T have angle a = mθ at vertex A, and angles b, c at the other two vertices. At the top of the iteration the check happens: if T happens to also have an angle exactly θ, the game stops and Mulan wins with 0 ≤ m − 1 cuts. Otherwise Mulan cuts to vertex A with either companion (say B) and parameter t = θ. *Validity:* m ≥ 2 gives 0 < θ < mθ = a, so t = θ ∈ (0, a), a legal move by the Cut Lemma. The pieces are
T₁ = (b, θ, a + c − θ)  and  T₂ = (c, (m − 1)θ, b + θ).
Shan-Yu keeps one of them; that piece is the current triangle at the top of the next iteration.
- If he keeps T₁: it has an angle equal to θ = 1·θ, so by the base case (applied at the next iteration) Mulan wins with 0 further cuts — total 1 ≤ m − 1 cuts (since m ≥ 2).
- If he keeps T₂: it has an angle equal to (m − 1)θ with 1 ≤ m − 1 < m, so by the induction hypothesis Mulan wins within (m − 1) − 1 = m − 2 further cuts — total 1 + (m − 2) = m − 1 cuts.
In both branches Mulan wins within m − 1 cuts. Note the argument does not care whether other angles of the kept piece are multiples — the induction hypothesis needs only *some* angle m′θ with m′ < m, which we exhibited. ∎

**Step 3: Forcing Lemma (closes G2).** *Suppose θ = 180°/n (n ≥ 2) and the current triangle T = (a, b, c) is safe. Then Mulan has a legal cut after which* **both** *pieces contain an angle that is a positive multiple of θ (so both pieces are unsafe; in fact each contains an angle mθ with 1 ≤ m ≤ n − 1).*

*Proof.* Since T is safe, by R1 the residues r_a = r(a), r_b = r(b), r_c = r(c) all lie in (0, θ).

*Mechanism.* Suppose Mulan can cut to some vertex — relabel it A, with angle a — with some companion — relabel it B, with angle b (legal for any choice of vertex and companion, by Cut Lemma (3)) — using the parameter
t = θ − r_b,
and suppose this t lies in (0, a) (validity, checked case by case below). Note t ∈ (0, θ) since r_b ∈ (0, θ), and t ≡ −r_b ≡ −b (mod θ). Then, by the Cut Lemma:
- Piece T₂ contains the angle b + t ≡ b − b = 0 (mod θ); it is positive, so by R1 it is a positive multiple of θ.
- Piece T₁ contains the angle a + c − t = 180° − (b + t) ≡ 0 − 0 = 0 (mod θ), using 180° ≡ 0 (mod θ); it is positive, so by R1 it is a positive multiple of θ.
Both displayed angles lie in (0°, 180°) by the Cut Lemma, so by O1 each equals mθ with 1 ≤ m ≤ n − 1. It remains to choose the cut vertex and companion so that t = θ − r_b ∈ (0, a). We have t > 0 always (r_b < θ), and t < θ; so it suffices to arrange **a ≥ θ** (then t < θ ≤ a). We split on n; the two cases n ≥ 3 and n = 2 are exhaustive since n ≥ 2.

*Case n ≥ 3 (θ ≤ 60°).* Let A be a vertex of maximal angle and B either other vertex. The maximal angle is at least the average: a ≥ 180°/3 = 60° ≥ θ. Hence t < θ ≤ a, so t ∈ (0, a): valid. ∎(case)

*Case n = 2 (θ = 90°).* Here "safe" means no angle is a positive multiple of 90°; since all angles are < 180°, the only positive multiple of 90° available is 90° itself, so safe ⟺ no angle equals 90° ⟺ T has no right angle. Also, for any angle x ∈ (0°, 90°) we have r_x = x. A triangle has at most one angle ≥ 90° (two would sum to ≥ 180°), so exactly one of the following two sub-cases holds (they are disjoint and, given no right angle, exhaustive):

- *Sub-case n = 2, T obtuse.* Let A carry the obtuse angle a > 90° and let B be either other vertex; then b < 90°, so r_b = b and t = 90° − b ∈ (0°, 90°) ⊂ (0, a): valid. The forced multiples are explicit: b + t = 90° and a + c − t = 180° − 90° = 90°.
- *Sub-case n = 2, T acute.* All angles are < 90°. Let A carry the largest angle a and B the second-largest angle b (ties broken arbitrarily); then the smallest angle c is at most the average 60°, so a + b = 180° − c ≥ 120° > 90°. Now t = 90° − r_b = 90° − b satisfies t > 0 (b < 90°) and t < a (equivalent to a + b > 90°, which holds): valid. Again b + t = 90° and a + c − t = 180° − 90° = 90°.

(For n = 2, both pieces thus contain the angle 90° = θ itself, so whichever piece is kept, the game stops at the next check: Mulan wins in exactly one cut. This is consistent with the general bound below since n − 1 = 1.) ∎

**Step 4: Assembly of Direction A (closes G3).** Let θ = 180°/n, n ≥ 2, and let T be the triangle at the top of any iteration (in particular Shan-Yu's arbitrary starting triangle T₀). Exactly one of the following holds (disjoint and exhaustive by construction):

1. **T has an angle equal to θ.** The check fires; Mulan wins with 0 cuts.
2. **T has no angle equal to θ, but some angle is a positive multiple of θ.** Then that angle is mθ with m ≥ 2 (m = 1 is excluded by the case hypothesis) and, by O1, m ≤ n − 1. By the Descent Lemma, Mulan wins within m − 1 ≤ n − 2 cuts.
3. **T is safe.** Mulan plays the Forcing Lemma cut: after it, *both* pieces contain a positive multiple of θ, and — by O1, since every angle of a triangle is < 180° = nθ — each such multiple is m′θ with 1 ≤ m′ ≤ n − 1. Whichever piece Shan-Yu keeps, the triangle at the top of the next iteration has an angle m′θ with m′ ≤ n − 1, so by the Descent Lemma Mulan wins within m′ − 1 ≤ n − 2 further cuts. Total: 1 + (n − 2) = n − 1 cuts.

In every case Mulan wins within max(0, n − 2, n − 1) = n − 1 cuts, whatever Shan-Yu does and whatever triangle he starts with. Direction A is proved. ∎

### Direction B: 180/θ ∉ ℤ ⟹ Shan-Yu can make the game last forever

**Step 5: Safe start exists (closes G4).** *If 0° < θ < 180°, there is a triangle that is safe for θ.* (This step does not need 180/θ ∉ ℤ.)

*Proof.* The set of positive multiples of θ below 180° is M = {mθ : m ∈ ℤ, 1 ≤ m < 180/θ}, which is finite: |M| ≤ ⌊180/θ⌋ < ∞. Consider the isoceles family T_α = (α, α, 180° − 2α) for α ∈ (0°, 90°): all three angles are positive and sum to 180°, so each T_α is a genuine triangle (realizable, e.g., as the triangle with base angles α). T_α fails to be safe only if α ∈ M or 180° − 2α ∈ M, i.e., only if α lies in the finite set M ∪ {(180° − μ)/2 : μ ∈ M}, of size at most 2⌊180/θ⌋. Since the interval (0°, 90°) is infinite, some α* ∈ (0°, 90°) avoids this finite set, and T_{α*} is safe. ∎

**Step 6: Safety Preservation Lemma (closes G5).** *Suppose 180/θ ∉ ℤ. If the current triangle T is safe, then for* **every** *legal Mulan cut — every choice of cut vertex, companion, and parameter — at least one of the two pieces is safe.*

(This lemma is also filed, self-contained, as `lemmas/safe-piece-exists.md`, proposed for certification. The proof here is inline and complete.)

*Proof.* By Cut Lemma (3), every legal move is described, after labeling, as: cut to vertex A (angle a) with companion B (angle b), parameter t ∈ (0, a), the third angle being c; the pieces are T₁ = (b, t, a + c − t) and T₂ = (c, a − t, b + t), and every angle appearing is in (0°, 180°). The labels (A, B, C) here range over all choices, so proving the claim for the triple in this notation proves it for every vertex and companion choice. Recall from Step 0: for these (positive) angles, "is a positive multiple of θ" ⟺ "≡ 0 (mod θ)" (R1), and congruence mod θ is compatible with addition and subtraction.

Suppose toward a contradiction (KB: Proof techniques — Contradiction) that both pieces are unsafe.

- T₁ = (b, t, a + c − t) unsafe means at least one of its three angles ≡ 0 (mod θ). Its inherited angle b is an angle of the safe triangle T, so b ≢ 0. Hence **t ≡ 0 or a + c − t ≡ 0 (mod θ)**.
- T₂ = (c, a − t, b + t) unsafe: its inherited angle c satisfies c ≢ 0 (T safe). Hence **a − t ≡ 0 or b + t ≡ 0 (mod θ)**.

This yields exactly four cases (a 2 × 2 disjunction; the cases need not be mutually exclusive, but they are exhaustive, and each leads to a contradiction — KB: Proof techniques — Casework):

(i) *t ≡ 0 and a − t ≡ 0.* Then a = t + (a − t) ≡ 0 + 0 = 0 (mod θ). Since a > 0, R1 makes a a positive multiple of θ — contradicting the safety of T.

(ii) *t ≡ 0 and b + t ≡ 0.* Then b = (b + t) − t ≡ 0 − 0 = 0 (mod θ); b > 0, so b is a positive multiple — contradicting safety of T.

(iii) *a + c − t ≡ 0 and a − t ≡ 0.* Then c = (a + c − t) − (a − t) ≡ 0 − 0 = 0 (mod θ); c > 0, so c is a positive multiple — contradicting safety of T.

(iv) *a + c − t ≡ 0 and b + t ≡ 0.* Then 180° = a + b + c = (a + c − t) + (b + t) ≡ 0 + 0 = 0 (mod θ), i.e., 180/θ ∈ ℤ — contradicting the hypothesis 180/θ ∉ ℤ.

All four cases are contradictory, so the assumption fails: at least one piece is safe. ∎

**Step 7: Assembly of Direction B (closes G6).** Assume 180/θ ∉ ℤ. Shan-Yu's strategy: start with a safe triangle T₀ (Step 5); whenever Mulan cuts, keep a safe piece (one exists by Step 6).

*Claim: for every integer k ≥ 0, the game reaches the top of iteration k + 1 with a safe current triangle T_k, and Mulan has not won.* Induction on k. Base k = 0: T₀ is safe by construction. Inductive step: suppose the triangle T_k at the top of iteration k + 1 is safe. A safe triangle has no angle equal to θ (θ = 1·θ is a positive multiple), so the check does not fire — Mulan does not win at iteration k + 1. Mulan then makes some legal cut; by the Safety Preservation Lemma at least one piece is safe, and Shan-Yu keeps such a piece, which is the triangle T_{k+1} at the top of iteration k + 2 — safe. This proves the claim for all k.

Hence for every k the game is still running after k iterations: the game never stops, and in particular Mulan cannot guarantee (indeed cannot achieve) victory in finitely many steps. Direction B is proved. ∎

### Step 8: Conclusion, answer, and verification

Combining Directions A and B:

**Answer.** Mulan can guarantee victory in finitely many steps exactly for
**θ ∈ { 180°/n : n ∈ ℤ, n ≥ 2 } = { 90°, 60°, 45°, 36°, 30°, (180/7)°, 22.5°, … }**,
i.e., exactly when 180/θ is an integer; and for θ = 180°/n she wins within n − 1 cuts. Note that every θ ∈ (0°, 180°) with 180/θ ∈ ℤ automatically has 180/θ ≥ 2, so the two phrasings agree; and every θ > 90° satisfies 180/θ ∈ (1, 2) ∌ ℤ, so all such θ fall under Direction B with no extra case needed.

**Verification (substitution checks, per the rigor rules).**

- *θ = 90° (n = 2).* Take any starting triangle. If it has a right angle, the check fires immediately. Otherwise it is safe (Step 3, case n = 2), and the Forcing cut makes both P-angles exactly 90°: e.g., T = (80°, 60°, 40°) is acute; cut to A (80°) with companion B (60°), t = 90° − 60° = 30° ∈ (0°, 80°); pieces (60°, 30°, 90°) and (40°, 50°, 90°) — both contain 90° = θ, so whichever Shan-Yu keeps, the next check fires. Mulan wins in 1 = n − 1 cut. ✓
- *θ = 40° (180/40 = 4.5 ∉ ℤ).* Multiples of 40° in (0°, 180°): {40°, 80°, 120°, 160°}. The triangle (55°, 55°, 70°) avoids all of them, so it is a safe start. (Note: (50°, 80°, 50°) would NOT do — 80° = 2·40°.) A sample cut: cut to the 70° vertex with companion a 55° vertex and t = 40°: pieces (55°, 40°, 85°) — unsafe, contains 40° — and (55°, 30°, 95°) — safe (30, 55, 95 ∉ {40, 80, 120, 160}); Shan-Yu keeps the safe one, as the Safety Preservation Lemma guarantees he always can. ✓

∎

## Promotable lemmas
- **safe-piece-exists** (Safety Preservation Lemma, Step 6 above) — *Statement:* Let 0° < θ < 180° with 180/θ ∉ ℤ, and let x ≡ y (mod θ) mean (x − y)/θ ∈ ℤ. Call a triangle safe if no angle is a positive integer multiple of θ. If T is safe, then for every legal cut (every vertex choice, companion labeling, and parameter t strictly inside the allowed interval), at least one of the two pieces is safe. — *Proved in full* inline in Step 6 of this file and, self-contained (with definitions, piece-formula derivation, relabeling remark, and full quantification), in `results/imo-2026-04/lemmas/safe-piece-exists.md` (proposed, awaiting proof-reviewer certification).
- **Cut Lemma** (Step 1 above) — realizability + piece-angle formula + relabeling; proved in full in Step 1 and reproduced inside the lemma file's setup. Reusable by any approach that manipulates the cut algebra.
