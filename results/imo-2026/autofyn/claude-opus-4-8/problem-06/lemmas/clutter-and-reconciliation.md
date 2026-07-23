# Certified shared lemmas — imo-2026-06 (reviewer-certified, round 2, from clique-descent)

Setup as in `bounded-gaps-and-clique.md`. Π={primes ≤ P₁} (P₁=largest prime factor of a₁);
a prime is small if ≤P₁, large if >P₁; σ(C)=C∩Π. 𝓜 = family of minimal clauses.
NOTE: this file uses the P₁ threshold (clique-descent's convention). Lemma S′ in
`shared-small-prime.md` uses the sharper a₁ threshold and SOLVES the crux these lemmas
only reduce; keep both for framing diversity.

## Lemma 1 (self-blocking clutter) — CERTIFIED
A nonempty prime-set T is a clause iff T is a transversal of 𝓜 (meets every minimal clause);
consequently 𝓜 is a clutter and 𝓜 = b(𝓜) (self-blocking).
Proof: T clause ⟺ T hits every clause (Cor E.1 with Tool 2) ⟺ T hits every minimal clause
(every clause contains a minimal one). So clauses = transversals of 𝓜; minimal clauses =
minimal transversals. ∎

## Proposition 2 (finite-ground-set reduction) — CERTIFIED
Let Q={large primes q : q∈C for some minimal clause C}. If Q is finite then 𝓜 is finite,
hence (certified finish) a_{n+T}=a_n+L for all n.
Proof: every minimal clause C ⊆ Π∪Q (each prime of C is small⇒∈Π, or large⇒∈Q); Π∪Q finite
⇒ finitely many subsets ⇒ 𝓜 finite. ∎  (Correct non-circular replacement of the retracted
false round-1 "Prop 1"; survives a₁=385 where 19 is a genuine large essential prime.)

## Lemma 3 (mutual witness) — CERTIFIED
Every large essential prime q∈Q lies in two distinct minimal clauses C,D with C∩D={q} and
σ(C),σ(D) disjoint nonempty. Hence Φ:Q→{disjoint nonempty shadow-pairs of Π}, q↦(σ(C_q),σ(D_q)),
has finite image, and Q finite ⟺ every fiber of Φ is finite.
Proof: pick minimal C∋q; it has a small prime p₀≠q, so C∖{q}≠∅ is a proper (non-clause) subset,
so (Lemma 1) misses some clause D₀; a minimal D⊆D₀ has D∩(C∖{q})=∅ ⇒ D∩C⊆{q}, and ≠∅ (Tool 2)
⇒ ={q}; p₀∈C∖D ⇒ C≠D; σ(C)∩σ(D)⊆{q}∩Π=∅. Finite image ⇒ fiber characterization. ∎

## Open gap (NOT certified)
"Q finite" / "Φ has finite fibers" is the remaining crux of clique-descent. It is CLOSED
independently by Lemma S′ (`shared-small-prime.md`), which proves every minimal clause ⊆
{primes ≤ a₁}, a finite ground set, forcing 𝓜 finite. As a standalone framing clique-descent
is still partial; its Lemmas 1–3 are reusable structure.
