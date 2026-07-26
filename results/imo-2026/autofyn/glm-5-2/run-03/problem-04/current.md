# IMO 2026 P4 — Mulan's Triangle Game

## Status
solved

## Approaches tried
- lattice-coset-descent (round 1) — full characterization, both directions. Necessity via four-coset intersection lemma (closure of the safe complement of L_θ); sufficiency via max-angle lattice-point entry cut + index-k descent. All sub-lemmas proved in full; n=2 / θ=90° handled separately; equilateral opening safe. — APPROVED (worked).
- altitude-halving (round 1) — Evan Chen route. Halving lemma (strong induction on k) + altitude round-up sufficiency (n≥3) with n=2 boundary; safe/unsafe necessity via external-angle identities (exhaustive four-case closure); equilateral defense. — APPROVED (worked).
- safe-unsafe-pairing (round 1) — deedy route. Necessity via four-coset closure (algebraic + external-angle geometric forms); sufficiency via round-up deficit function, deficit-sum lemma (d-sum ∈ {θ,2θ}), refined pairing lemma (cyclic-sum contradiction; one-top case), pairing cut, k-descent; n=2 direct 90°-trick. Genuinely different entry mechanism from the other two. — APPROVED (worked).

## Current best
Complete rigorous proof of the characterization: Mulan can guarantee victory in finitely many steps if and only if θ = 180°/n for some integer n ≥ 2. Three independent complete proofs (max-angle lattice-point entry, altitude + round-up, deficit-pairing) all establish the same sufficiency; the canonical four-coset closure establishes necessity in all three. Move bound ≤ n−1 (approaches 1, 3) or ≤ n (approach 2, looser but finite).

## Full proof

**Theorem (answer).** *Mulan can guarantee victory in finitely many steps, regardless of how Shan-Yu plays, if and only if θ = 180°/n for some integer n ≥ 2.*

Three independent complete proofs were certified this round; the cleanest (max-angle lattice-point entry + index-k descent) is recorded below. The other two (altitude-halving, safe-unsafe-pairing) are equivalent in the necessity direction and give alternative sufficiency entry mechanisms; see their approach files.

---

### 1. Reduction to the angle game

The only data of the current triangle T that any move can affect or reveal is its angle triple (a,b,c) with a+b+c=180° and a,b,c>0; side lengths are irrelevant to whether some angle equals θ and to the angles of either child produced by a straight cut. Hence the game is entirely played on S = {(a,b,c): a,b,c>0, a+b+c=180°}.

**Cut-geometry lemma.** In △ABC with ∠A=a, ∠B=b, ∠C=c, Mulan may cut to vertex A by selecting P on side BC (not a vertex); the cut AP splits △ABC into two triangles with angle triples
$$\triangle ABP:\;(x,\;b,\;a+c-x),\qquad \triangle ACP:\;(a-x,\;c,\;b+x),$$
where x = ∠BAP ∈ (0,a). Conversely every x ∈ (0,a) is realizable.

*Proof.* Write the two sub-angles at A as ∠BAP=x and ∠PAC=a−x with 0<x<a. In △ABP the angles are x (at A), b (at B, since P∈BC so ∠ABP=∠ABC=b), and 180°−b−x = a+c−x (at P). In △ACP the angles are a−x (at A), c (at C), and 180°−c−(a−x)=b+x (at P). The two angles at P sum to (a+c−x)+(b+x)=180°, as they must (supplementary at the straight cut). As P moves along BC from B to C, the ray AP rotates continuously, so x=∠BAP is a continuous function taking all values in (0,a) (IVT between limiting values 0 and a). ∎

By relabeling, Mulan may cut to any of the three vertices. Winning condition: some angle equals θ.

### 2. The lattice L_θ and the safe complement

Define L_θ = {(a,b,c)∈S : some one of a,b,c lies in θZ_{>0}} (positive integer multiples). A state is **safe** (for Shan-Yu) if it is not in L_θ. Since θ∈θZ_{>0}, every winning state lies in L_θ; in particular a safe state has no angle equal to θ, so Mulan has not won from a safe state.

### 3. NECESSITY — four-coset intersection lemma

**Lemma A (closure of the safe set).** Let (a,b,c)∈S be safe and suppose 180°∉θZ_{>0} (equivalently θ≠180°/n for every integer n≥2). Then for every vertex at which Mulan cuts and every parameter x in the legal range, at least one of the two children is again safe.

*Proof.* Relabel so the cut is to vertex A with parameter x∈(0,a), producing C1=(x,b,a+c−x), C2=(a−x,c,b+x). All six entries are positive. Since (a,b,c) is safe, b∉θZ_{>0} and c∉θZ_{>0}, so:
- C1∈L_θ iff x∈θZ_{>0} OR (a+c−x)∈θZ_{>0};
- C2∈L_θ iff (a−x)∈θZ_{>0} OR (b+x)∈θZ_{>0}.

"C1∈L_θ AND C2∈L_θ" is a conjunction of two two-term disjunctions, hence the disjunction of four pairwise conjunctions. Settle each:

**(i)** x∈θZ_{>0} and (a−x)∈θZ_{>0}: x=mθ, a−x=pθ ⟹ a=(m+p)θ∈θZ_{>0}, contradicting a safe.
**(ii)** x∈θZ_{>0} and (b+x)∈θZ_{>0}: x=mθ, b+x=pθ; b+x>x (b>0) ⟹ p>m ⟹ b=(p−m)θ∈θZ_{>0}, contradicting b safe.
**(iii)** (a+c−x)∈θZ_{>0} and (a−x)∈θZ_{>0}: a+c−x=mθ, a−x=pθ; a+c−x>a−x (c>0) ⟹ m>p ⟹ c=(m−p)θ∈θZ_{>0}, contradicting c safe.
**(iv)** (a+c−x)∈θZ_{>0} and (b+x)∈θZ_{>0}: adding, (a+c−x)+(b+x)=a+b+c=180°=(m+p)θ ∈θZ_{>0}, contradicting 180°∉θZ_{>0}.

The four cases exhaust the conjunction; each leads to a contradiction. Hence no choice of vertex and parameter makes both children land in L_θ; at least one child is safe. ∎

**Corollary (Shan-Yu's defense).** If θ≠180°/n for every integer n≥2, Shan-Yu prevents Mulan from ever winning: open equilateral and, after every Mulan cut, keep a safe child.

*Proof.* Assume θ≠180°/n, so 180°∉θZ_{>0}. The equilateral (60°,60°,60°) is safe: 60°=mθ ⟹ 180°=3·60°=3mθ∈θZ_{>0} (3m≥3≥2), contradicting 180°∉θZ_{>0}. Inductive invariant: the current state is safe. Initially true (equilateral). If the current state is safe, by Lemma A at least one child is safe regardless of Mulan's play; Shan-Yu keeps such a child. By induction the state is safe forever. A safe state has no angle equal to θ, so Mulan never wins. ∎

This establishes **necessity**: if θ is not of the form 180°/n, Mulan cannot guarantee victory.

### 4. SUFFICIENCY — entering L_θ in one move (lattice-point entry cut)

Assume henceforth θ=180°/n for an integer n≥2, so 180°=nθ∈θZ_{>0}.

**Lemma B (lattice-point-in-open-interval).** Let (a,b,c)∈S be a state with no angle a positive multiple of θ (a Phase-1 state). Relabel so A≥B≥C are the three angles in non-increasing order. Then there exists an integer k with 1≤k≤n−1 such that kθ∈(C, A+C).

*Proof.* Split on n.
- **n≥3 (θ≤60°).** A≥60° (max of three positives summing to 180°). Claim A>θ: suppose A≤θ; then every angle ≤A≤θ and, being a non-multiple (Phase-1), each is <θ, so 180°=a+b+c<3θ≤nθ=180°, contradiction. The interval (C,A+C) has length A>θ. Since C is not a multiple of θ, C/θ∉Z; let m=⌈C/θ⌉≥1. Then mθ>C (strictly, C non-multiple) and mθ<C+θ<C+A (θ<A), so mθ∈(C,A+C). Finally mθ<A+C<180°=nθ gives m<n, i.e. k=m≤n−1.
- **n=2 (θ=90°).** The only positive multiple of θ below 180° is 90° itself (k=1). Need 90°∈(C,A+C), i.e. C<90°<A+C=180°−B. C<90°: at most one angle of a triangle can be ≥90° (two would sum to ≥180°, leaving the third ≤0°), and C is the minimum. B<90°: if B≥90° then A≥B≥90°, so A+B≥180°, forcing C≤0°, impossible; hence B<90°, i.e. 90°<A+C. (Covers the equilateral (60,60,60), a Phase-1 state for n=2: 60<90<120.) ∎

**Corollary C (Phase-1 entry).** From any Phase-1 state, Mulan forces both children into L_θ in one move.

*Proof.* Relabel A≥B≥C. By Lemma B pick k∈{1,…,n−1} with kθ∈(C,A+C), and set x=A+C−kθ. The inequalities C<kθ<A+C give 0<x<A, a legal cut at vertex A. The cut-geometry lemma gives C1=(x,B,A+C−x), C2=(A−x,C,B+x). Using A+B+C=180°=nθ: C1's third angle = A+C−x = kθ∈θZ_{>0}; C2's third angle = B+x = B+A+C−kθ = 180°−kθ = (n−k)θ∈θZ_{>0} (n−k≥1 since k≤n−1). Both children lie in L_θ, regardless of which Shan-Yu discards. (Positivity: x>0, A−x=kθ−C>0, both marked angles positive.) ∎

### 5. SUFFICIENCY — index-k descent within L_θ

**Lemma D (forced descent).** Suppose the current state has an angle jθ for j∈{2,…,n−1}, the other two angles being b,c (jθ+b+c=180°). Mulan plays so that Shan-Yu is forced to hand her a new state with an angle (j−1)θ.

*Proof.* Mulan cuts to the vertex carrying angle jθ with parameter x=θ (legal: 0<θ<jθ since j≥2). The cut-geometry lemma gives C1=(θ,b,(j−1)θ+c) and C2=((j−1)θ,c,b+θ). C1 contains θ: if Shan-Yu keeps C1 the game stops and Mulan wins. To postpone defeat Shan-Yu must keep C2, which carries (j−1)θ. C2 is a valid triangle (all entries positive, sum (j−1)θ+c+b+θ=jθ+b+c=180°). ∎

**Corollary E (Mulan wins from any state when θ=180°/n).** If θ=180°/n, n≥2, Mulan wins in at most n−1 moves from any state.

*Proof.* From the current state: (a) if some angle equals θ — already won (0 moves); (b) if some angle equals jθ for j∈{2,…,n−1} — apply Lemma D repeatedly; the index j drops by 1 each forced move, reaching 1 (angle θ) after j−1≤n−2 moves; (c) if no angle is a positive multiple of θ (Phase-1) — play Corollary C (1 move), after which both children lie in L_θ; whichever Shan-Yu keeps carries jθ with 1≤j≤n−1; if j=1 done (1 move total), if j≥2 apply Lemma D (≤j−1≤n−2 more moves). Total worst case 1+(n−2)=n−1. ∎

This establishes **sufficiency**: for every θ=180°/n, n≥2, Mulan guarantees victory in finitely many (≤n−1) moves.

### 6. Conclusion

- **Necessity** (§3): if θ≠180°/n for every integer n≥2, Shan-Yu opens equilateral and maintains a safe state forever, so Mulan cannot guarantee a win.
- **Sufficiency** (§4–5): if θ=180°/n for an integer n≥2, Mulan wins in at most n−1 moves from any opening, regardless of Shan-Yu's play.

Therefore **Mulan can guarantee her victory in finitely many steps if and only if θ = 180°/n for some integer n ≥ 2.** ∎

---

### Alternative certified proofs

Two further independent complete proofs are in the approach files, equivalent in the necessity direction (same four-coset closure), with genuinely different sufficiency entry mechanisms:

- `approaches/altitude-halving.md` — Evan Chen route: halving lemma (strong induction on k) + altitude-to-right-triangle step + round-up cut (45<kθ≤90) for n≥3, with the n=2 boundary handled directly. Move bound ≤n.
- `approaches/safe-unsafe-pairing.md` — deedy route: round-up deficit function d(x)=m_xθ−x, deficit-sum lemma (d(a)+d(b)+d(c)∈{θ,2θ}), refined pairing lemma (cyclic-sum contradiction in the no-top case; one-top case via a+b<θ), pairing cut (both children marked in one move), k-descent; n=2 direct 90°-trick. Move bound ≤n−1.
