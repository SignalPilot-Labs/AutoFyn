# Approach: self-blocking-clutter-induction

## Status
partial

## Approaches tried
- (round 1, outline) Opened. Same proved reduction; the core finiteness was to be attacked as a pure clutter-theory theorem ("every identically self-blocking clutter of finite sets on a countable ground set is finite") by induction on the minimum member size τ, with link/cross-blocking structure. Base case τ = 1 and the k = 2 witness-through-b structure were proved; the inductive step was GAP B.
- (round 1, build) **Executed the outline-reviewer's directive: tried to refute the pure theorem before building the induction — and REFUTED it.** There is an explicit infinite identically self-blocking clutter of finite sets on a countable ground set (the "ladder clutter", full proof below, brute-force sanity-checked by computer on truncations: 0 failures). Consequently **GAP B is unclosable and this approach, as scoped, is a dead end**: no purely combinatorial proof of "M finite" can exist, because the combinatorial axioms M was shown to satisfy (intersecting antichain + self-covering + witness lemma + trace/dodging analogs) do not imply finiteness. The counterexample moreover satisfies every *clutter-level* consequence extracted so far by the rival approaches, so it is a certified no-go lemma for the whole field: any successful closing of the finiteness gap must use the number-theoretic realization (integers, windows, sizes/densities) in an essential way.

## Current best

Two proved items:

1. **The shared reduction stands** (imported from approaches/valid-set-sunflower-core.md, Steps 1–4 and 6, verified independently by the round-1 outline review): the problem is equivalent to the finiteness of the clutter M of inclusion-minimal types, and M is an intersecting antichain of finite sets with the self-covering property (every finite set meeting all members of M contains a member of M), satisfying in addition the witness lemma (4c) and the dodging consequence (4b).

2. **No-go theorem (proved in full below).** The purely combinatorial statement "every identically self-blocking clutter of finite sets on a countable ground set is finite" is **false**. Hence the finiteness of M cannot be deduced from the clutter-level properties alone; the open gap of the field (GAP 1 / GAP A / GAP B — all the same statement "M is finite") must be closed with number-theoretic input.

Open gap for the problem itself: "M is finite" remains unproved. This approach contributes the boundary of what cannot work; it does not close the gap.

---

## The no-go theorem (full proof)

### Definitions

Let Ω be a countable ground set. A **clutter** on Ω is a family M of nonempty *finite* subsets of Ω forming an antichain under inclusion (no member contains another). A finite set X ⊆ Ω is a **transversal** of M if X ∩ Y ≠ ∅ for every Y ∈ M. Following the usage fixed by the shared foundation (Step 3 corollary of valid-set-sunflower-core.md), M is **identically self-blocking** if

- (S1) M is intersecting: any two members meet; and
- (S2) self-covering: every finite transversal of M contains a member of M.

(As proved in the shared foundation, and re-proved in Lemma 6 below, (S1)+(S2)+antichain imply that the members of M are exactly the inclusion-minimal finite transversals of M, i.e. b(M) = M; this is the property enjoyed by the minimal-type clutter M of the IMO problem.)

**Theorem (Ladder counterexample).** There exists an **infinite** identically self-blocking clutter of finite sets on a countable ground set. Moreover it satisfies the witness lemma, and it possesses a two-element set E₀ meeting every member such that for every finite B ⊆ Ω ∖ E₀ some member of M is disjoint from B.

### The construction

Let G be the one-way infinite ladder: vertex set {u₀, u₁, u₂, …} ∪ {v₀, v₁, v₂, …}, with edges

- rungs r_i = u_i v_i (i ≥ 0),
- top rails a_i = u_i u_{i+1} (i ≥ 0),
- bottom rails b_i = v_i v_{i+1} (i ≥ 0).

All these edges are distinct; G is connected (every vertex is joined to u₀ by a path along the rails and one rung) and every vertex has degree ≤ 3. Set s := u₀, t := v₀ (adjacent via r₀). Let E := E(G), a countable set.

- **L₁** := the family of edge sets of simple s–t paths in G. Each is a finite nonempty subset of E.
- **L₂** := the family of **minimal finite s–t cuts**: finite C ⊆ E such that G − C has no s–t path ("C is a cut"), and no proper subset of C is a cut.

Take two new symbols 1, 2 ∉ E, put Ω := {1, 2} ∪ E, and define

**M := { {1,2} } ∪ { {1} ∪ P : P ∈ L₁ } ∪ { {2} ∪ C : C ∈ L₂ }.**

### Lemma 1 (M is infinite)

For each k ≥ 0 let D_k := {r₀, r₁, …, r_k, a_k}. Then D_k ∈ L₂, and the D_k are pairwise distinct; hence L₂, and with it M, is infinite.

*Proof.* D_k = δ(S_k), the set of edges of G with exactly one endpoint in S_k := {u₀, …, u_k} (the edges leaving S_k are exactly r₀,…,r_k and a_k; the rails a₀,…,a_{k−1} lie inside S_k). D_k is a cut: s ∈ S_k, t ∉ S_k, and any s–t path starts in S_k and ends outside it, so at its first vertex outside S_k it traverses an edge with exactly one endpoint in S_k, i.e. an edge of D_k; thus G − D_k has no s–t path.

Minimality — every edge of D_k is essential:

- Removing r_i (0 ≤ i ≤ k) from D_k: the path u₀ →(a₀)→ u₁ → ⋯ →(a_{i−1})→ u_i →(r_i)→ v_i →(b_{i−1})→ ⋯ →(b₀)→ v₀ uses only the edges a₀,…,a_{i−1}, r_i, b₀,…,b_{i−1}; of these, only r_i lies in D_k (the a_j used have j ≤ i−1 < k, and no b_j ∈ D_k). So this path avoids D_k ∖ {r_i}, which is therefore not a cut.
- Removing a_k: the path u₀ →(a₀…a_k)→ u_{k+1} →(r_{k+1})→ v_{k+1} →(b_k…b₀)→ v₀ uses a₀,…,a_k, r_{k+1}, b₀,…,b_k and avoids D_k ∖ {a_k} = {r₀,…,r_k}. So that set is not a cut.

Hence no proper subset of D_k obtained by deleting one element is a cut; since cuts are upward closed among finite edge sets (removing more edges preserves the absence of an s–t path — Lemma 2(ii)), no proper subset at all is a cut (a proper subset is contained in some D_k ∖ {e}, and a superset of a cut is a cut, so D_k ∖ {e} would be a cut). Thus D_k is a minimal finite cut. The D_k are pairwise distinct (a_k ∈ D_k determines k). ∎

### Lemma 2 (elementary facts about paths and cuts)

(i) A finite T ⊆ E meets every member of L₁ **iff** T is a cut.
(ii) If C is a cut and C ⊆ C′ ⊆ E with C′ finite, then C′ is a cut. ("Upward closed.")
(iii) Every finite cut contains a minimal finite cut.
(iv) If s and t lie in the same component of the spanning subgraph (V(G), T) for a finite T ⊆ E, then T contains the edge set of a simple s–t path.
(v) L₁ is an antichain, and L₂ is an antichain.

*Proof.* (i) T meets every simple s–t path iff no simple s–t path avoids T iff G − T has no s–t path (any s–t walk in G − T contains a simple s–t path in G − T) iff T is a cut. (ii) G − C′ is a subgraph of G − C, so it has no s–t path either. (iii) Let C be a finite cut. Repeatedly delete from C any element e such that C ∖ {e} is still a cut; the process terminates since C is finite, ending at a cut C′ ⊆ C such that C′ ∖ {e} is not a cut for any e ∈ C′. Then no proper subset D ⊊ C′ is a cut: pick e ∈ C′ ∖ D; if D were a cut then by (ii) its finite superset C′ ∖ {e} ⊇ D would be a cut, contradiction. So C′ is a minimal finite cut. (iv) Standard: a walk from s to t using only edges of T exists (same component); a shortest such walk repeats no vertex (else splice out the cycle to get a shorter one), hence is a simple path, and its edges all lie in T. (v) L₁: suppose P ⊆ P′ for simple s–t paths P ≠ P′; then their edge sets differ, and since a simple path is determined by its edge set (the edge set of a simple path spans a subgraph in which s and t have degree 1 and inner vertices degree 2, and this subgraph IS the path), P ⊆ P′ with P ≠ P′ means there is e ∈ P′ ∖ P. Deleting e from the path P′ splits its edge-spanned subgraph into two sub-paths, one containing s and one containing t, with no edge of P′ ∖ {e} joining them; but P ⊆ P′ ∖ {e} connects s to t (P is an s–t path) — contradiction. So P = P′. L₂: immediate from minimality: if C ⊊ C′ with both minimal cuts, C′ has a proper subset that is a cut, contradiction. ∎

### Lemma 3 (crux: transversals of the cuts contain paths)

If a finite T ⊆ E meets every member of L₂ (every minimal finite cut), then T contains the edge set of a simple s–t path.

*Proof.* Suppose not. By Lemma 2(iv), s and t lie in different components of the spanning subgraph (V(G), T). Let S be the vertex set of the component of s in (V(G), T); then t ∉ S. Since T is finite, S is finite (a connected graph on vertex set S using only edges of T has |S| ≤ |T| + 1). Let

δ(S) := { e ∈ E : e has exactly one endpoint in S }.

- **δ(S) is finite:** every vertex of G has degree ≤ 3 and S is finite, so |δ(S)| ≤ 3|S|.
- **δ(S) ∩ T = ∅:** if e = xy ∈ T with x ∈ S, then y is joined to x by a T-edge, hence lies in the same T-component, so y ∈ S and e ∉ δ(S).
- **δ(S) is a cut:** s ∈ S, t ∉ S; any s–t path in G starts in S and ends outside, so at its first vertex outside S it uses an edge with exactly one endpoint in S, i.e. an edge of δ(S). Hence G − δ(S) has no s–t path. (In particular δ(S) ≠ ∅, since the s–t path with edge set {r₀} must meet it.)

By Lemma 2(iii), δ(S) contains a minimal finite cut C₀, and C₀ ∩ T ⊆ δ(S) ∩ T = ∅. So T misses the member C₀ of L₂ — contradicting the hypothesis. ∎

### Lemma 4 (M is an intersecting antichain of finite nonempty sets)

*Proof.* Finiteness and nonemptiness of members are clear. **Intersecting:** {1}∪P and {1}∪P′ share 1; {2}∪C and {2}∪C′ share 2; {1,2} meets everything through 1 or 2; and ({1}∪P) ∩ ({2}∪C) ⊇ P ∩ C ≠ ∅ because C is a cut and P a path, so P meets C by Lemma 2(i). **Antichain:** within each of the three groups: {1,2} is alone; {1}∪P vs {1}∪P′ reduces to L₁ being an antichain (Lemma 2(v)); {2}∪C vs {2}∪C′ likewise. Across groups: {1}∪P ⊄⊅ {2}∪C since 1 ∉ {2}∪C and 2 ∉ {1}∪P; {1,2} ⊆ {1}∪P would need 2 ∈ P ⊆ E, false, and {1}∪P ⊆ {1,2} would need P ⊆ {2}, false since P ⊆ E is nonempty; symmetrically for {2}∪C. ∎

### Lemma 5 (M is self-covering: property (S2))

Every finite transversal T ⊆ Ω of M contains a member of M.

*Proof.* T meets the member {1,2}, so 1 ∈ T or 2 ∈ T. Cases (exhaustive and disjoint):

**(a) 1 ∈ T and 2 ∈ T.** Then the member {1,2} ⊆ T. ✓

**(b) 1 ∈ T, 2 ∉ T.** For every C ∈ L₂, T meets the member {2} ∪ C; since 2 ∉ T, we get (T ∩ E) ∩ C ≠ ∅. So the finite edge set T ∩ E meets every minimal finite cut; by Lemma 3 it contains the edge set P₀ of a simple s–t path. Then the member {1} ∪ P₀ ⊆ T. ✓

**(c) 2 ∈ T, 1 ∉ T.** For every P ∈ L₁, T meets the member {1} ∪ P; since 1 ∉ T, T ∩ E meets every simple s–t path, so by Lemma 2(i) T ∩ E is a finite cut, and by Lemma 2(iii) it contains a minimal finite cut C₀. Then the member {2} ∪ C₀ ⊆ T. ✓

**(d) 1 ∉ T and 2 ∉ T.** Impossible: T would miss the member {1,2}. ∎

### Lemma 6 (the remaining self-blocking half, and the witness lemma, hold for free)

Let N be any clutter (antichain of finite nonempty sets) satisfying (S1) and (S2). Then:

(i) every member of N is a minimal transversal of N, and every minimal finite transversal is a member — i.e. b(N) = N;
(ii) (witness lemma) for every Y ∈ N and y ∈ Y there is W ∈ N with W ∩ Y = {y}.

*Proof.* (i) A member A is a transversal by (S1) (it meets every member, including itself). It is minimal: if A ∖ {a} were a transversal, by (S2) it would contain a member B ⊆ A ∖ {a} ⊊ A, contradicting the antichain property. Conversely a minimal finite transversal X contains a member B by (S2); B is itself a transversal (just shown), so minimality of X forces X = B ∈ N. (ii) Y ∖ {y} is not a transversal (as in (i)), so some W ∈ N has W ∩ (Y ∖ {y}) = ∅; and W ∩ Y ≠ ∅ by (S1); hence W ∩ Y = {y}. ∎

### Proof of the Theorem

By Lemmas 4 and 5, M satisfies (S1), (S2) and is an antichain of finite nonempty sets on the countable ground set Ω; by Lemma 1 it is infinite; by Lemma 6 it is identically self-blocking (b(M) = M) and satisfies the witness lemma. For the last clause take E₀ := {1, 2}: every member of M meets E₀ by construction, and for any finite B ⊆ Ω ∖ E₀ the member {1,2} is disjoint from B. ∎

**Sanity check (not part of the proof).** A brute-force verification on truncations of the ladder (levels ≤ 8, minimal cuts enumerated from both the s-side and the t-side, all 2¹¹ candidate sets X ⊆ {1,2} ∪ E(levels ≤ 2)) confirmed: all enumerated minimal cuts contain r₀; every tested transversal of the minimal-cut family contains an s–t path (Lemma 3: 292 cases, 0 failures); every tested finite transversal of M contains a member (Lemma 5: 1023 cases, 0 failures); and D₀,…,D₅ are minimal cuts.

---

## Consequences for the field (why this is a no-go lemma, and what survives)

The ladder clutter M satisfies **every clutter-level property so far extracted from the IMO problem's minimal-type clutter**:

1. intersecting antichain of finite sets on a countable ground set — Lemma 4;
2. self-covering / identically self-blocking (Step 3 corollary of the shared foundation) — Lemmas 5–6;
3. the witness lemma (4c) — Lemma 6(ii);
4. the *clutter-level consequence* of the dodging lemma (4b) — "there is a finite E₀ meeting every member, and for every finite B disjoint from E₀ some member of M avoids B": holds with E₀ = {1,2} and the member {1,2}. (Note: in the number-theoretic setting this consequence is likewise trivially witnessed by the minimum member A itself. The nontrivial content of dodging is *where the avoiding terms sit* — in every window of length g — which has no clutter-level formulation.)
5. Consistency with the proved sunflower kill (5b): in the ladder clutter, the trace-{1} subfamily (paths) and the trace-{2} subfamily (cuts) both have **unbounded member sizes** — exactly the case (5c) that remained open. So (5b) is not contradicted; rather, the ladder shows the (5c) configuration is genuinely realizable and **GAP 1 cannot be closed from properties 1–4 alone**.

Therefore:

- **GAP B is dead**: the target theorem of this approach is false; no induction on τ (or any other pure argument) can prove it.
- **Any proof of "M is finite" must use the realization into the integers** beyond properties 1–4. Levers that genuinely have no ladder analog and remain candidates:
  - *Window/location control*: dodging (4b) actually produces an avoiding term inside **any prescribed CRT-compatible window of length g**, not merely "somewhere"; the ladder has no notion of windows.
  - *Sizes and densities*: each member X is realized only by integers divisible by ∏_{p∈X} p; V ⊇ (multiples of g) has density ≥ 1/g and bounded gaps; the set {m : P(m) ⊇ X} has density 1/∏_{p∈X} p. A counting attack ("infinitely many minimal types force V to miss long runs, contradicting bounded gaps (4a)") uses exactly what the ladder lacks. This matches the outline-review's suggested fourth line.
  - *Small-prime lock-in* (the rival crt-window-small-prime-lockin target ∪M ⊆ E₀ = {p ≤ g}): in the ladder clutter ∪M is infinite, so this statement is **not** derivable from 1–4 either — consistent with (and an explanation of) why that approach must argue with integers, as it already does.

## Cases to cover
Not applicable any more to this slug's original plan (the induction is cancelled). The no-go theorem's own casework (Lemma 5: four cases by T ∩ {1,2}) is complete above.

## Watch out for
- Do not re-attempt a purely combinatorial closing of the finiteness gap under any disguise (links, cross-blocking pairs, Ramsey on incidence, sunflower refinements *alone*): the ladder clutter refutes all of them at once. Any new lemma proposed for GAP 1 should first be tested against the ladder clutter — if the ladder satisfies its hypotheses, the lemma is false or useless.
- When enumerating minimal cuts of the ladder computationally, cuts around **t** (finite side containing t, e.g. {r₀, b₀} = δ({v₀})) must be included, not only cuts around s — omitting them produces false "counterexamples" to Lemma 3 (this happened and was diagnosed in round 1).

## Promotable lemmas
- **No-go: infinite identically self-blocking clutters exist (ladder clutter).** Statement: there is an infinite antichain M of finite nonempty subsets of a countable ground set Ω such that M is intersecting, every finite transversal of M contains a member, b(M) = M, the witness lemma holds, and there is a 2-element E₀ ⊆ Ω meeting every member such that for each finite B ⊆ Ω ∖ E₀ some member avoids B. Proved in full in this file (Theorem + Lemmas 1–6), computer-sanity-checked. Reusable as a hypothesis-filter for every future attack on the "M finite" gap.
