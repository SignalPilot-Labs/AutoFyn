# Approach: valid-set-sunflower-core

## Status
partial

## Approaches tried
- (round 1, outline) Opened. Reduction chain written with full proofs; core finiteness attacked via trace pigeonhole + infinite sunflower lemma; bounded-size case settled in outline, unbounded-size case left as GAP 1.
- (round 1, build) Polished the whole reduction per outline-review notes (sunflower lemma proved inline, antichain edge cases written out, β-extraction made airtight and simplified — the witness lemma is not even needed for it). Extracted the shared foundation into `lemmas/terms-equal-valid-set.md`, `lemmas/dodging-and-witness.md`, `lemmas/finite-core-implies-periodicity.md`. **Two new proved tools:** the Locality Lemma (greedy rejection is witnessed by a smaller term — the genuinely dynamic constraint not visible in the pure clutter abstraction) and the **König transversal-tree theorem (Step 5d)**, which strictly subsumes the bounded-size kill and sharpens the enemy of GAP 1 to a single explicit infinite object (an increasing branch of minimal partial transversals). GAP 1 itself still open. Failed attacks this round, recorded so they are not retried:
  - *Density / AP-covering:* try to trap a fixed positive-density arithmetic progression of terms inside ∪_{q ∈ R(Y)} qℤ for infinitely many members Y and let the densities multiply out to 0. **Dies on the intersecting property:** any explicit AP of terms one constructs has modulus divisible by rad(Z') for some member Z', and every Y ∈ M meets Z', so a single shared prime of Y ∩ Z' covers the whole AP for free. Covering statements alone can never contradict an intersecting family; minimality must enter quantitatively.
  - *Self-referential CRT dodge:* dodge the big primes of the branch set T_x with a window below x and contradict "every term ≤ x is hit by T_x". Fails: to dodge the (unboundedly many) big primes of T_x by CRT one must place the window at position ~∏(those primes) ≫ x, where T_(window) has strictly more primes than T_x — the new primes may cover the dodging terms. No contradiction without controlling *where new branch primes come from*.
  - *Pure clutter route:* (P1) antichain + (P2) pairwise intersecting + (P3) every finite transversal contains a member — equivalently the dichotomy "every finite X either contains a member or is disjoint from one" — may well admit infinite examples (a forcing-style construction looks plausible); per the outline-review this refutation attempt belongs to `self-blocking-clutter-induction`. This approach therefore now routes the number-theoretic Locality Lemma into the crux rather than betting on the pure statement.

## Current best
Complete rigorous reduction of the whole problem to the single claim **"M is finite"** (Steps 1–4 and 6, now formalized in the three `lemmas/` files), plus, toward that claim: the bounded-size kill (Step 5b), the β-extraction chain (5c), the Locality Lemma (5d′ = L1.5), and the König transversal-tree theorem (5d) with its corollaries, which reduce GAP 1 to ruling out one explicit infinite branch object (properties (i)–(vii) below). Open gap: derive a contradiction from that branch (GAP 1, sharpened form stated at the end of Step 5).

## Proof (complete except for the single marked gap)

**Target (the problem's claim).** Let a_1 < a_2 < ... be the greedy sequence: an infinite sequence of integers > 1 such that for every n ≥ 1, a_{n+1} is the smallest integer > a_n with gcd(a_{n+1}, a_i) > 1 for all i = 1, ..., n. Prove there exist positive integers T, L with a_{n+T} = a_n + L for **all** n ≥ 1.

**Notation.** P(m) = set of primes dividing m; P_k := P(a_k); "term" = a value of the sequence; V, H\*, M as in `lemmas/terms-equal-valid-set.md`. Labels (L1.x), (L2.x) refer to the proposed lemma files.

### Steps 1–3 (foundation — proved)
Proved in `lemmas/terms-equal-valid-set.md`:
- (L1.1) any two terms share a prime;
- (L1.2) {terms} = V, and for m ≥ a_1: m is a term ⟺ P(m) ∈ H\*;
- (L1.3) H\* = {types of terms}; every X ∈ H\* is the type of arbitrarily large terms (realization p_1^j · p_2 ⋯ p_r);
- (L1.4) H\* is upward closed, pairwise intersecting; every X ∈ H\* contains a member of M; X ∈ H\* ⟺ X is a transversal of M ⟺ X contains a member of M; and X ∉ H\* ⟺ some Z ∈ M is disjoint from X;
- (L1.5) **Locality:** if m > a_1 and m ∉ V, some term t < m has gcd(t, m) = 1.

### Step 4 (bounded gaps, dodging, witnesses — proved)
Fix A ∈ M of minimum size, g := ∏_{p ∈ A} p, E₀ := {primes ≤ g} (finite; A ⊆ E₀). Proved in `lemmas/dodging-and-witness.md`:
- (L2.1) every multiple of g that is ≥ a_1 is a term; every interval (x, x+g], x ≥ a_1, contains a term;
- (L2.2) for any finite set B of primes all > g there are arbitrarily large terms t with P(t) ∩ B = ∅;
- (L2.3) for Y ∈ M, ρ ∈ Y there is W ∈ M with W ∩ Y = {ρ};
- (L2.4) every Z ∈ M meets A, hence meets E₀.

### Step 6 (finite core ⟹ the claim, for all n — proved)
Proved in `lemmas/finite-core-implies-periodicity.md`: if M is finite then with E := ∪M, L := ∏_{p∈E} p, T := |V ∩ [a_1, a_1+L)|, we have a_{n+T} = a_n + L for **all** n ≥ 1, and T, L are positive integers. (The "for all n" requirement dissolves because by (L1.2) the sequence *is* the increasing enumeration of V from its least element, and x ↦ x+L is an order isomorphism V → V ∩ [a_1+L, ∞).)

**Hence the whole problem reduces to Step 5: M is finite.**

### Step 5 (core finiteness) — the one remaining gap

**Claim: M is finite.**

Suppose for contradiction M is infinite. All of 5a–5d below is fully proved; the contradiction is completed except in the final case, marked GAP 1.

#### 5a. Trace pigeonhole (proved)
By (L2.4) every Z ∈ M has Z ∩ E₀ ≠ ∅. Since E₀ is finite there are at most 2^{|E₀|} possible traces Z ∩ E₀, so some nonempty σ ⊆ E₀ has

  N₀ := { Y ∈ M : Y ∩ E₀ = σ } infinite.

Write R(Y) := Y ∖ E₀ (the *big part*; all its primes are > g, since every prime ≤ g lies in E₀). For distinct Y, Y′ ∈ N₀ we have R(Y) ≠ R(Y′) (equal traces and equal big parts would force Y = Y′). At most one Y ∈ N₀ has R(Y) = ∅: if R(Y) = R(Y′) = ∅ then Y = σ = Y′. Discard it if present; N₀ remains infinite, and now every Y ∈ N₀ satisfies σ ⊊ Y.

#### 5b. The bounded-size case (proved): no infinite subfamily of N₀ has uniformly bounded size

**Lemma S (infinite sunflower lemma, Erdős–Rado, infinite version).** *Let s ≥ 0 and let F be an infinite family of distinct finite sets, each of size ≤ s. Then F contains an infinite sunflower: an infinite subfamily {F_i}_{i≥1} and a set C (the core) with F_i ∩ F_j = C for all i ≠ j.*

*Proof, by induction on s.* If s = 0 then F ⊆ {∅} is not infinite — vacuous. Let s ≥ 1 and assume the statement for s − 1.

Case 1: some element p lies in infinitely many members of F. Let F′ := { F ∖ {p} : F ∈ F, p ∈ F }. Distinct members F ≠ G containing p give F ∖ {p} ≠ G ∖ {p}, so F′ is an infinite family of distinct finite sets of size ≤ s − 1. By induction it contains an infinite sunflower {F_i ∖ {p}} with core C′. Then {F_i} is an infinite sunflower in F with core C′ ∪ {p}: for i ≠ j, F_i ∩ F_j = ((F_i∖{p}) ∩ (F_j∖{p})) ∪ {p} = C′ ∪ {p}.

Case 2: every element lies in only finitely many members. Build F_1, F_2, ... recursively: pick any F_1 ∈ F; having picked pairwise disjoint F_1, ..., F_k, note that the set of members meeting F_1 ∪ ... ∪ F_k is finite (that union has ≤ ks elements, each meeting only finitely many members), so infinitely many members are disjoint from all of F_1, ..., F_k; pick F_{k+1} among them. The result is an infinite pairwise disjoint subfamily — a sunflower with core C = ∅. ∎

**5b proper.** Suppose infinitely many Y ∈ N₀ satisfy |Y| ≤ s. Their big parts R(Y) are distinct finite sets of size ≤ s, so by Lemma S there are Y_1, Y_2, ... ∈ N₀, pairwise distinct, whose big parts form an infinite sunflower: R(Y_i) = C ⊔ π_i with core C and pairwise disjoint petals π_i = R(Y_i) ∖ C.

*Petals are nonempty, after discarding at most one member:* if π_i = π_j = ∅ for i ≠ j then R(Y_i) = C = R(Y_j), contradicting distinctness of big parts; so at most one petal is empty — discard that member, keeping infinitely many, all with π_i ≠ ∅.

Now σ ∪ C ⊆ σ ∪ R(Y_1) = Y_1 and the inclusion is strict (π_1 ≠ ∅). By minimality of Y_1 ∈ M, σ ∪ C ∉ H\*. By (L1.4d) there is G ∈ M with G ∩ (σ ∪ C) = ∅. But G must meet every Y_i (L1.4b), and G ∩ Y_i ⊆ Y_i ∖ (σ ∪ C) = π_i. So the finite set G meets infinitely many pairwise disjoint petals π_i — impossible. ∎

Consequently (still under "M infinite"): in N₀, only finitely many members have size ≤ s for each s, i.e., **sizes in N₀ tend to infinity** along any enumeration.

#### 5c. β-extraction (proved): an infinite chain of big primes, each in infinitely many members

**Claim.** There exist pairwise distinct primes β_1, β_2, ... , all > g, and infinite subfamilies N₀ ⊇ N_1 ⊇ N_2 ⊇ ... such that for every m ≥ 1:
 (i) σ ∪ {β_1, ..., β_m} ⊆ Y for every Y ∈ N_m;
 (ii) σ ∪ {β_1, ..., β_m} ∉ H\*.

*Proof.* We show by induction on m ≥ 0 (with N as given, B_0 := ∅): if N_m ⊆ N₀ is infinite and every Y ∈ N_m contains σ ∪ B_m where B_m = {β_1, ..., β_m} (m distinct primes > g), then σ ∪ B_m ∉ H\*, and there is a prime β_{m+1} ∉ σ ∪ B_m, β_{m+1} > g, lying in infinitely many Y ∈ N_m; setting N_{m+1} := { Y ∈ N_m : β_{m+1} ∈ Y } completes the step.

First, σ ∪ B_m ∉ H\*. Otherwise, by (L1.4c), σ ∪ B_m would contain some member Z ∈ M; then Z ⊆ σ ∪ B_m ⊆ Y for every Y ∈ N_m, and since M is an antichain and Y ∈ M, this forces Y = Z for every Y ∈ N_m — impossible, as N_m is infinite while Z is a single set. This proves (ii) at stage m; in particular the base case statement "σ ∉ H\*" (m = 0) also holds by this argument (every Y ∈ N₀ properly contains σ).

By (L1.4d) pick G_m ∈ M with G_m ∩ (σ ∪ B_m) = ∅. For every Y ∈ N_m, G_m ∩ Y ≠ ∅ (L1.4b), and

  G_m ∩ Y ⊆ Y ∖ (σ ∪ B_m) = R(Y) ∖ B_m  (using Y = σ ∪ R(Y) and G_m ∩ σ = ∅, G_m ∩ B_m = ∅).

So every Y in the infinite family N_m meets the *finite* set G_m in a prime of R(Y) ∖ B_m. Pigeonhole over the finitely many elements of G_m: some β_{m+1} ∈ G_m lies in R(Y) for infinitely many Y ∈ N_m. This β_{m+1} is > g (it lies in a big part), and β_{m+1} ∉ σ ∪ B_m (it lies in G_m, which avoids σ ∪ B_m) — in particular it is distinct from β_1, ..., β_m. ∎

(Note the reviewer's requested airtightness: the fresh witness G_m is *chosen disjoint from σ ∪ {β_1,...,β_m}* by (L1.4d) applied to the non-hitting set σ ∪ B_m, so the fresh prime is automatically new.)

#### 5d. König transversal-tree theorem (proved this round): the enemy is a single infinite branch

This subsumes 5b/5c and localizes the remaining difficulty. For x ≥ a_1 let

  Q(x) := { P(t) : t a term, t ≤ x } — a finite, nonempty family of finite prime sets (nonempty since a_1 ≤ x; finite since there are ≤ x terms below x).

Call a finite prime set T a *transversal of Q(x)* if T ∩ Q ≠ ∅ for all Q ∈ Q(x), and *minimal* if no proper subset is one.

**Fact 1.** Every minimal transversal T of Q(x) satisfies T ⊆ U(x) := ∪ Q(x) = {primes dividing some term ≤ x}, a finite set. *Proof:* an element γ ∈ T ∖ U(x) meets no Q ∈ Q(x), so T ∖ {γ} is still a transversal, contradicting minimality. Hence Q(x) has finitely many minimal transversals (all are subsets of the finite set U(x)). ∎

**Fact 2.** Every X ∈ H\* contains a minimal transversal of Q(x). *Proof:* X is a transversal of Q(x) (X hits every term type). Among subsets of X that are transversals of Q(x), pick T of minimum cardinality; then T is minimal (a proper transversal subset of T would be a smaller subset of X). ∎

**Fact 3 (node kill).** If T is a finite prime set with T ∈ H\* and T ⊆ Y for infinitely many Y ∈ M, then we have a contradiction. *Proof:* by (L1.4c) take Z ∈ M, Z ⊆ T. Then Z ⊆ Y for infinitely many Y ∈ M; since M is an antichain this forces Y = Z each time — impossible for more than one Y. ∎

**Theorem K.** Suppose M is infinite. Then there exist finite prime sets T_x, one for each integer x ≥ a_1, such that:
 (i) T_x is a minimal transversal of Q(x);
 (ii) T_x ⊆ T_{x+1} for all x, and |T_x| → ∞;
 (iii) T_x ∉ H\* for every x;
 (iv) for each x, infinitely many Y ∈ M satisfy T_x ⊆ Y;
 (v) every element of T_x is a prime ≤ x dividing some term ≤ x;
 (vi) every term t is divisible by some prime of T_t (indeed of T_x for every x ≥ t);
 (vii) the traces T_x ∩ E₀ are nondecreasing in x and hence equal to a fixed nonempty σ\* ⊆ E₀ for all x ≥ some x₁; moreover σ\* ∩ A ≠ ∅, and for x ≥ x₁ all elements of T_x ∖ σ\* are primes > g.

*Proof.* Build a graph on nodes (x, T), where x ≥ a_1 is an integer and T is a minimal transversal of Q(x) such that N_T := { Y ∈ M : T ⊆ Y } is infinite.

*Levels are nonempty.* Fix x. Every Y ∈ M lies in H\*, so by Fact 2 it contains some minimal transversal of Q(x). There are finitely many minimal transversals (Fact 1) and infinitely many Y ∈ M, so by pigeonhole some minimal transversal T of Q(x) is contained in infinitely many Y — i.e., (x, T) is a node.

*Parents.* Let (x+1, T′) be a node. Since Q(x) ⊆ Q(x+1) (as families — every term ≤ x is a term ≤ x+1), T′ is a transversal of Q(x); as in Fact 2, T′ contains a minimal transversal T of Q(x). And N_T ⊇ N_{T′} is infinite. So (x, T) is a node with T ⊆ T′. Choose, once and for all, one such parent for each node at each level > a_1. This makes the node set a forest in which every node at level x+1 has exactly one parent at level x; iterating parents, every node at level x descends from a (unique, along chosen parents) root at level a_1.

*König's infinity lemma.* Each level is finite (Fact 1) and nonempty, so there are infinitely many nodes and finitely many roots; some root r has infinitely many descendants. Now recursively construct an infinite path: start at r; given a node v with infinitely many descendants, its descendants other than v itself are distributed among its finitely many children (children of v = nodes at the next level whose chosen parent is v), so some child has infinitely many descendants; move to it. This yields nodes (x, T_x) for all x ≥ a_1 with T_x ⊆ T_{x+1} (parenthood is inclusion).

*Properties.* (i), (iv), (v) hold by nodehood and Fact 1. (iii): if some T_x ∈ H\*, Fact 3 with (iv) gives an immediate contradiction; so T_x ∉ H\*. For (ii): inclusions hold by construction; the sizes |T_x| are nondecreasing; if they were bounded, the chain T_x would be eventually constant, equal to some fixed T (a strictly increasing inclusion raises the size). That T would be a transversal of every Q(x), i.e., T ∩ P(t) ≠ ∅ for every term t, i.e., T ∈ H\* (T is nonempty as it hits P(a_1), and finite) — contradicting (iii). So |T_x| → ∞. For (vi): if t ≤ x then P(t) ∈ Q(x) and T_x ∩ P(t) ≠ ∅. For (vii): T_x ∩ E₀ ⊆ T_{x+1} ∩ E₀ are nondecreasing subsets of the finite set E₀, hence eventually constant, say = σ\* for x ≥ x₁. σ\* ∩ A ≠ ∅ (hence σ\* ≠ ∅): by (L1.3) there are arbitrarily large terms t with P(t) = A; take such a t ≥ x₁; by (vi), T_t ∩ P(t) = T_t ∩ A ≠ ∅; since A ⊆ E₀ we get T_t ∩ A ⊆ T_t ∩ E₀ = σ\*, and also T_t ∩ A ⊆ A, so σ\* ∩ A ⊇ T_t ∩ A ≠ ∅. Finally for x ≥ x₁, an element of T_x ∖ σ\* is not in E₀, i.e., is a prime > g. ∎

**Corollary K1 (relation to 5b/5c).** Theorem K shows the *global* structure directly: if M is infinite at all, there is an infinite strictly growing chain of minimal partial transversals, each contained in infinitely many members. Restricting K(ii),(iv) to the members containing T_x recovers a β-chain of the kind produced in 5c (the elements of T_x ∖ σ\*, x ≥ x₁, are distinct primes > g each lying in infinitely many members). 5b is kept above as an independent kill of the bounded-size case; K is strictly more informative than 5c.

**Corollary K2 (preloading).** Let Γ := ∪_x T_x and Γ′ := Γ ∖ E₀ (an infinite set of primes > g, by K(ii),(vii)). Then for every x ≥ x₁:
 (a) T_x ∉ H\*, so by (L1.4d) there is Z_x ∈ M with Z_x ∩ T_x = ∅;
 (b) **every** member Z ∈ M with Z ∩ T_x = ∅ contains a branch prime that enters the branch strictly after level x: there are y > x and γ ∈ Z ∩ (T_y ∖ T_x) with γ ∈ Γ′.

*Proof of (b).* By (L1.3) there are arbitrarily large terms t with P(t) = Z; pick one with t > x (≥ x₁). By K(vi), T_t ∩ Z ≠ ∅; pick γ in it, and set y := t. Since σ\* ⊆ T_x (x ≥ x₁) and Z ∩ T_x = ∅, we get γ ∉ σ\*, so γ ∈ T_t ∖ σ\* ⊆ Γ′ by K(vii); and γ ∉ T_x since γ ∈ Z. ∎

So the branch is "self-sustaining": every member that dodges the branch's current finite state carries a future branch prime. This is the exact shape of the obstruction.

#### GAP 1 (sharpened form — the only unproven step)

**Open claim.** The infinite branch of Theorem K cannot exist; i.e., there is no chain (T_x)_{x ≥ a_1} with properties K(i)–(vii). Equivalently (given 5a–5d): M is finite.

What is known about the enemy (all proved above): all its elements at level x are primes ≤ x dividing terms ≤ x (K(v)); it covers every term at its own scale (K(vi)); its small-prime content freezes at σ\* ∋ (a prime of A) while infinitely many primes > g accrue (K(ii),(vii)); every finite state is non-hitting yet contained in infinitely many minimal members (K(iii),(iv)); and members dodging any finite state must pre-carry future branch primes (K2). The Locality Lemma (L1.5) — non-membership of m in V is always witnessed by a term < m — is proved and available, and is the number-theoretic resource the pure clutter abstraction lacks; it has not yet been successfully coupled to the branch. Routes already tried and dead this round are recorded under *Approaches tried*.

### Conclusion (conditional)
Steps 1–4 and 6 are complete. Once Step 5 (finiteness of M) is closed, `lemmas/finite-core-implies-periodicity.md` yields positive integers T and L with a_{n+T} = a_n + L for all n ≥ 1, proving the problem. The problem's `answer_type` is `none`; no numeric answer is required.

## Open gaps
- GAP 1 (sharpened, Step 5): rule out the König branch — equivalently, prove M finite in the unbounded-size case. Everything else is complete and formalized.

## Promotable lemmas
Proved in full this round and written as proposed lemma files for reviewer certification:
- **terms-equal-valid-set** (`lemmas/terms-equal-valid-set.md`): (L1.1) pairwise sharing; (L1.2) {terms} = V; (L1.3) realization H\* = {types}; (L1.4) self-blocking/transversal equivalences; (L1.5) Locality Lemma. Proved there in full.
- **dodging-and-witness** (`lemmas/dodging-and-witness.md`): (L2.1) bounded gaps; (L2.2) CRT dodging of finite sets of primes > g; (L2.3) witness lemma; (L2.4) nonempty small trace. Proved there in full.
- **finite-core-implies-periodicity** (`lemmas/finite-core-implies-periodicity.md`): M finite ⟹ the full problem claim, with explicit T, L. Proved there in full.
- **Infinite sunflower lemma (Lemma S)** — proved in full in Step 5b of this file; reusable verbatim; could be certified as `lemmas/infinite-sunflower.md` if the reviewer prefers a separate file.
- **Theorem K (König transversal tree)** — proved in full in Step 5d of this file; it is the sharpest currently-certifiable statement toward GAP 1 and is import-ready for the rival approaches (both `crt-window-small-prime-lockin` and `self-blocking-clutter-induction` can use K(vi), K(vii), K2 directly).

## Watch out for
- The Δ_n guardrail: no argument may assume a universal bound on member sizes; only the infinitude of M is to be excluded.
- Any covering/density attack must use minimality quantitatively; plain covering statements are absorbed by the intersecting property (see failed attempts).
- The pure clutter statement (finiteness from (P1)–(P3) alone) is possibly false; do not re-attempt purely combinatorial closures without new structure — route (L1.5) or window arithmetic into the branch.
