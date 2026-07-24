# Approach: confluence-newman

## Status
partial

## Target (whole problem)
(a) exactly one M>1 remains after finitely many moves; (b) M is choice-independent.

## Technique (the spine)
**Abstract Rewriting System (ARS) + Newman's Lemma.** States = size-2026 multisets of integers ≥1;
one move = one rewrite step. Part (a) = strong normalization (termination) + terminal states have ≤1
entry >1; part (b) = **uniqueness of normal form**, obtained from *confluence*. Newman's Lemma:
`strongly normalizing + locally confluent ⇒ confluent ⇒ unique normal form`. This is a genuinely
different *framing* from the closed-form invariant route — it proves M unique WITHOUT computing
`∏ p^{g_p}`, by showing all reduction paths converge.

## Skeleton
1. **ARS setup.** State = multiset `{x_1,…,x_2026}`, each `x_i ≥ 1`. Rewrite `S → S'`: pick i≠j with
   `x_i,x_j>1`, replace by `gcd, lcm/gcd`. Normal form = state with no available move = ≤1 entry >1.
2. **Strong normalization (part a, termination).** Same lex monovariant `(Ω_total, C)` as
   `perprime-valuation` step 2 strictly decreases each step ⇒ every rewrite sequence is finite ⇒
   normal forms exist and are reached.
3. **Local confluence (WCR) — the crux.** If `S → S1` and `S → S2` (two different moves), show S1, S2
   have a common reduct. Critical-pair analysis by how the two chosen position-pairs `{i,j},{k,l}`
   overlap:
   - **Disjoint:** the two moves act on disjoint cells ⇒ they commute; apply the other move to each of
     S1,S2 to reach one common T in one step. (Clean.)
   - **Share one position** (three cells x,y,z): the only nontrivial critical pair. Reduce to the
     3-entry sub-board and show the two divergent results are joinable.
   - **Same pair:** identical move, no divergence.
4. **Newman's Lemma.** SN (step 2) + WCR (step 3) ⇒ confluent ⇒ every state has a unique normal form.
   Applied to the initial board ⇒ the terminal multiset is unique ⇒ M is unique (part b).
5. **Exactly one survivor.** As in `perprime-valuation` step 5: some prime has invariant `g_p≥1`, so a
   normal form cannot be all-1's; with ≤1 entry >1 ⇒ exactly one.

## Key lemmas (claim + mechanism)
- **Newman's Lemma** — NOT in knowledge_base.md; must be *stated and proved from scratch* (standard
  well-founded-induction proof: induct on the terminating order; use WCR at the first divergence, then
  the induction hypothesis on the smaller states). This is extra machinery this route must carry.
- **Commutation of disjoint moves** — moves on disjoint cells change disjoint coordinates, so order is
  irrelevant (the map on a cell depends only on that cell's pair).
- **3-cell joinability (the real gap)** — for three entries `x,y,z`, "combine (x,y) then continue" and
  "combine (y,z) then continue" reach a common reduct.

## Open gaps (builder fills)
- G1 (**hardest, honest flag**): local confluence on the 3-cell critical pair. Explorer's Python check
  ({4,6,9}: branches {2,6,9} and {3,4,6}) shows the two branches do **NOT** meet at any single
  intermediate state — they only agree at the *terminal* normal form. So the naive one-step "diamond"
  FAILS: WCR here is *not* one-step joinability but multi-step joinability. To prove even that, the
  cleanest known argument is to show both branches share, for every prime p, the same
  `g_p = gcd_i v_p(x_i)` (invariant) and then invoke SN+induction — i.e. this route almost certainly
  must **import the per-prime gcd invariant (Lemma L2 of perprime-valuation)** to close G1. Builder
  should either (i) prove multi-step local confluence via the invariant, or (ii) prove Newman's Lemma
  in the "each branch reaches a normal form and they're equal because g_p matches" form (semi-decision:
  this collapses toward the closed-form route's crux).
- G2: prove Newman's Lemma (or the specialized induction) rigorously with the terminating order of
  step 2 as the well-founded relation.
- G3: strong normalization details = perprime-valuation G3/G4.

## Cases to cover
- Critical-pair overlap: disjoint / share-one-position / same-pair (only share-one is nontrivial).
- 3-cell sub-board: sizes ordering of x,y,z (Euclidean-invariance is uniform, so no real sub-casework,
  but must argue uniformity).

## Watch out for
- **Local confluence is subtle here:** there is no one-step diamond (branches meet only at the end).
  Do not assert one-step WCR — it is false. The honest content is multi-step joinability certified by
  the invariant, so this framing is *heavier* than perprime-valuation for the same crux (the
  subtractive-Euclid gcd fact). Its value is diversity + a uniqueness proof that never names the
  closed form.
- Newman's Lemma must be justified, not cited from KB (absent there).
- "Exactly one survivor" still needs the g_p≥1 invariant fact (shared with the primary route).
</content>
