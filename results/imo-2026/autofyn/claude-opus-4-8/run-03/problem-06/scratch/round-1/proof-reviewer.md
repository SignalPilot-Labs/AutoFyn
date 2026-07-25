# Proof-review — imo-2026-06, round 1

Two approaches reviewed independently. Both verdicts below; workspace `current.md`
set to **partial** (best of the two). Counterexample and structural claims verified
by independent simulation (sympy greedy build).

---

## Slug 1: anomaly-count-terminates — RETHINK (Status: unsolved)

**Scores:** Correctness of the *framing* = fatally broken; correctness of the salvaged
lemmas = high; Progress = negative on the main line, positive on infrastructure.

The builder honestly refuted its own crux. I reproduced the refutation independently:
- Greedy sequence for `a_1 = 375` (P={3,5}, M=rad=15) is periodic with **(T,L)=(852,3990)**;
  `a_{n+852}=a_n+3990` holds over 2000 computed terms. `3990 = 2·3·5·7·19`, so **19 | L**
  while `M = 15`. The "confinement" lemma `p|L ⇒ p≤M` is therefore **FALSE**, and the
  `>M` sole-witness "anomalies" recur with positive density (19 | 60/852 terms per period),
  so they are **infinite**. The intended monovariant/rigidity upgrade does not exist.

The approach as framed (any M-threshold on structural primes) cannot work — confirmed.
Recorded Status (`unsolved`) is correct. → **RETHINK**: back to the outliner. The builder's
own recommendation (seed a genuinely different framing not routed through an M/K threshold)
is sound; note that its "corrected crux" (finite `primes(L)`) is the SAME wall as slug 2's
Finite Alphabet crux, so a mere re-route would collapse onto slug 2.

**Certified from this approach:** free lemmas (Anchor, Gap bound, Distance–prime) — proved
correctly (see `lemmas/free-lemmas.md`). The conditional **Reduction Lemma** (finite fixed
modulus K + fixed admissible residue set U ⇒ periodicity) is correct but is subsumed by
slug 2's cleaner endgame; not separately certified. **Negative result recorded** in
`current.md`: the confinement lemma is false — no approach may import it.

---

## Slug 2: redundant-constraint-antichain — CHANGES REQUESTED (Status: partial)

**Scores:** Correctness = high (every written step valid); Completeness = one clean
open crux; Progress = major — reduces the FULL problem, for all n≥1, to a single finiteness
statement, with the notorious no-transient/"eventual ⇒ all n" difficulty fully dissolved.

I adversarially re-derived the load-bearing steps and checked them numerically.

**Load-bearing step re-derived independently — the no-transient closure (L7+L8) is CORRECT:**
- L4 (pairwise-intersecting): `gcd(a_i,a_j)>1` ∀i≠j — immediate from the defining clause at
  the smaller index. Valid.
- L6 (domination): every `F_i` contains a global ⊆-minimal support, and any `c` meeting all
  of `𝓐_∞` is admissible at every stage, so `A ⊆ A_n`. The minimal element of
  `{G∈𝓕 : G⊆F_i}` is genuinely minimal in all of `𝓕` (any strict refinement would also lie
  in `F_i`). Valid.
- L7 (every term in A): each `F∈𝓐_∞` equals some `F_j`; L4 gives `F_k∩F_j≠∅`, so `a_k` meets
  every minimal support, i.e. `a_k∈A`. Valid.
- L8: (≤) `s(a_n)∈A⊆A_n`, `>a_n` ⇒ `a_{n+1}≤s(a_n)`; (≥) `a_{n+1}∈A`, `>a_n`, `s` least ⇒
  `a_{n+1}≥s(a_n)`. Hence **`a_{n+1}=s(a_n)` for ALL n≥1** — no transient, no reversibility
  step. This is airtight and genuinely closes the step the outline feared.
- Endgame (L9–Cor11): conditional on `Π` finite, `A` is a union of residues mod `L₀=∏Π`,
  the sequence enumerates `{c∈A : c≥a_1}` in order, and stepping through the `m=|ρ(A)|`
  residues advances by exactly `L₀`, giving `a_{n+m}=a_n+L₀` for all n. Valid.

**Independent numerical confirmation (a_1=105):** minimal supports {2,3},{2,5},{2,7},{3,5,7};
Π={2,3,5,7}, L₀=210; every term meets every minimal support (L7=True); every term in A;
`a_{n+1}=s(a_n)` with no A-element skipped; `|ρ(A)|=58=T`, matching the observed period
`a_{n+58}=a_n+210`. Also confirmed a_1=375's period agrees with this framework (Π must contain 19).

**Non-circularity check:** `A` is defined via the whole infinite family `𝓕`; L7/L8 use no
finiteness. Only the endgame invokes `Π` finite. The reduction is sound and non-circular.
The recorded Status (`partial`) is correct.

**Residual gap (the ONLY open step):**
> **Crux (Finite Alphabet):** `𝓐_∞` (the ⊆-minimal prime-supports of `𝓕`) is finite,
> equivalently `Π=⋃𝓐_∞` is a finite set of primes.
The builder's §7 gives honest partial progress (reformulation via small companion, a correct
proof that L4+Anchor alone do NOT force finiteness, pigeonhole to a fixed anchor prime + a
counting tension) but does NOT close it. This is a real gap. → **CHANGES REQUESTED**: next
round attacks the Finite Alphabet crux (the counting/growth-vs-density mechanism bounding how
many distinct primes can ever enter minimal supports).

**Certified lemmas** (→ `lemmas/`):
- `free-lemmas.md` — Anchor, Gap bound (gap≤M, a_n=Θ(n)), Distance–prime, Pairwise-intersecting.
- `no-transient-fixed-successor.md` — L7+L8: `a_k∈A ∀k`, `a_{n+1}=s(a_n) ∀n≥1`, hence finite Π
  ⇒ periodicity from n=1 with T=|ρ(A)|, L=∏Π. The key transplantable result — removes the
  "eventual ⇒ all n" step for any route that establishes a finite support alphabet.

---

## Summary
- redundant-constraint-antichain: **CHANGES REQUESTED** (partial) — sole gap = Finite Alphabet crux.
- anomaly-count-terminates: **RETHINK** (unsolved) — M-threshold confinement refuted; re-plan.
- `current.md` Status = **partial**. Both approaches now share the single Finite Alphabet wall;
  per the plateau rule, next round should seed a genuinely different framing to attack it.
