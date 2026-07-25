# Approach: a-periodic-sole-witness

## Status
unsolved (new skeleton, round 2)

## Idea in one line
Do NOT prove the Finite Alphabet crux (𝓐_∞ finite). Prove the strictly WEAKER target that
suffices for the whole theorem: **A is periodic** (a finite union of residue classes mod some
finite L). Attack it via the certified fact density(A) ≥ 1/M > 0 plus the observation that A
is periodic **iff only finitely many primes are ever a "sole witness"** — a condition strictly
weaker than "finitely many primes appear in minimal supports," and provably immune to the
p*-anchored obstruction that kills the antichain/density route.

## Why this is a genuinely different top-level target (not a patch on the antichain approach)
Certified: everything reduces to "A = {c : c meets every F ∈ 𝓐_∞} is a union of finitely many
residue classes mod some L" — that plugs straight into Lemmas 9–11 of
`redundant-constraint-antichain` (which only ever use that A is periodic mod *some* modulus,
not that 𝓐_∞ is finite) and, with the certified no-transient lemma, gives a_{n+T}=a_n+L for
ALL n. So **A periodic ⇒ full theorem.**

A periodic is *strictly weaker* than 𝓐_∞ finite:
- 𝓐_∞ finite ⇒ A periodic (Lemma 9). Not conversely.
- The recorded obstruction family {{p*}∪{q} : q large} (§7b of antichain) has **infinite** 𝓐_∞,
  yet A = {c : ∀q (p*|c or q|c)} = exactly the multiples of p*, which IS periodic (mod p*).
  So the p*-anchored infinite antichain — which pigeonhole shows is the ONLY way 𝓐_∞ can be
  infinite (§7c) — does NOT break periodicity of A. The obstruction that kills the antichain
  route is invisible to this target. That is the whole point.

## Key definitions
- A prime p is a **sole witness** if there exist an admissible c ∈ A and a minimal support
  F ∈ 𝓐_∞ with F(c) ∩ F = {p} (c meets F through p and through no other prime of F).
- Let Q := { p : p is a sole witness }.

## Skeleton
1. **Membership in A is determined mod rad(Q ∪ P).** [Lemma] If p ∉ Q and p ∉ P... more
   precisely: whether c ∈ A depends only on the set F(c) ∩ Q_A, where Q_A is the set of
   *relevant* primes. Prove: prime p is relevant to A (∃ c,c' differing only in p-divisibility
   with c∈A, c'∉A) **iff** p ∈ Q. — by definition-chase: dropping p from c drops c out of A iff
   p was a sole witness for some F.
2. **If Q is finite, A is periodic mod L := ∏_{p∈Q} p.** — by Step 1, c∈A depends only on
   {p∈Q : p|c}, i.e. only on c mod L (each p∈Q divides L). Nonempty (mult. of M ⊆ A). [GAP-FREE
   once Step 1 holds.]
3. **Q is finite.** [THE CRUX — see Open gaps.] Candidate mechanism: density monovariant.
   The stage-n admissible sets A_n = {c : c meets F_i ∀i≤n} satisfy A_1 ⊇ A_2 ⊇ ... ⊇ A,
   so density(A_n) is **non-increasing** and bounded below by density(A) ≥ 1/M > 0 (certified).
   A prime p enters Q only at a term a_i that is a sole witness — an integer sharing exactly one
   prime (namely p) with some earlier term. Show each *new* sole-witness prime forces a genuine
   (non-redundant) drop in density(A_n), and that the total available density drop is finite
   (bounded by 1 − 1/M), so only finitely many new sole-witness primes can occur.
4. **Conclude.** Q finite ⇒ (Step 2) A periodic mod L ⇒ (Lemmas 9–11 + no-transient, certified)
   a_{n+T}=a_n+L for all n. ∎

## Open gaps (the builder must close, or the reviewer must flag as still-open crux)
- **Step 3 is the crux.** The naive "sum of per-prime densities" is recorded DEAD (density
  explorer): a prime's density-drop is not disjoint/additive across primes. The NEW ingredient
  this target buys: unlike "appears in a minimal support," a **sole-witness** prime p forces c
  to be *coprime to F∖{p}* for some minimal F — a much stronger, more rigid condition. The hard
  step is to prove: a sole-witness prime p contributes a density loss that is NOT masked by any
  other prime (because sole-witness = the ONLY witness, so removing p genuinely ejects a positive
  density of residues from A). Must show the masking that saves the p*-family (there q is never a
  sole witness) cannot happen for a genuine sole witness. This is where the p*-obstruction is
  proved harmless. **If this density-loss-is-real lemma holds, Σ (losses) ≤ 1 − 1/M forces |Q|<∞.**

## Watch out for
- Do NOT claim density(A_n) → 0 (refuted: p*-family keeps density = 1/p*). The argument must be
  "each NEW SOLE-WITNESS prime costs ≥ ε_p density that is genuinely lost (not recovered later),"
  with Σ ε_p ≤ 1. The per-prime cost ε_p may shrink with p; convergence Σε_p ≤ 1−1/M must be
  argued, not assumed finite-count.
- Sole-witness is about A (global 𝓐_∞), not about stage-n. Keep the ∀-quantifier over 𝓐_∞ honest.
- Verify Step 1's "iff" in both directions on the a_1=375 data: 19 must come out as a sole
  witness (it does: {2,5,19} minimal, a term meets it only via 19 sometimes), Q={2,3,5,7,19}, so
  A periodic mod 2·3·5·7·19 = 3990 = L. Matches certified (T,L)=(852,3990). Good consistency check.
