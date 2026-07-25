# Build report — anomaly-count-terminates (imo-2026-06)

## Status: UNSOLVED — approach refuted as framed.

## Headline (Spec concern — must reach the outliner)
The approach's two load-bearing claims are **FALSE**, exhibited by a concrete,
partly hand-checkable counterexample **`a_1 = 375`** (`P = {3,5}`, `M = ∏P = 15`):

1. **Confinement `p | L ⇒ p ≤ M` is FALSE.** Direct 4000-term computation:
   the sequence is periodic with `(T, L) = (852, 3990)`, `3990 = 2·3·5·7·19`, so
   **`19 | L` while `19 > M = 15`.** (Verified `a_{n+852} = a_n + 3990` over the
   whole computed range.)
2. **"`>M` sole-witness anomalies are finite" is FALSE.** `19` is a sole witness at
   a positive-density set of steps (60 of every 852 terms are multiples of 19; the
   sole-witness role recurs each period) ⇒ **infinitely many anomalies.**
3. **The "rigidity" upgrade is invalid (it was the confinement lemma in disguise).**
   The outline said a persistent large sole-witness `q` forces `q|L ⇒ q ≤ M`,
   contradiction. In fact `q = 19 | L` and this is *not* a contradiction — it is the
   stable regime. The step `q|L ⇒ q ≤ M` is exactly the false confinement claim.

Hand-checkable anomaly (no computer needed): `a_1=375 → 375,378,380,384,390,396,399`.
At `n=6`, `a_7 = 399 = 3·7·19`. `a_3 = 380 = 2²·5·19` has small support `{2,5}`, but
`399` is odd with `5∤399`, so `399` meets `380`'s constraint **only via `19 > M`**;
the small-only prediction is `400 = 2⁴·5²`, and `399 < 400` because `19` rescues it.

Why the reviewer's sim missed it: `375` is a rare seed (my scan `2..700` found it as
the **only** anomalous seed). "0 anomalies on tested seeds" was undersampled.

## What I proved (fully rigorous, salvageable)
- **Anchor**, **Gap bound / linear growth (`a_{n+1}-a_n ≤ rad(a_1)`, `a_n=Θ(n)`)**,
  **Distance–prime** — complete proofs in the approach file. Framing-agnostic.
- **Reduction Lemma** (complete): *If* a finite prime set `S` (modulus `K=∏S`) and a
  fixed admissible residue set `U ⊆ Z/K` exist with, for `n ≥ N₀`, admissibility on
  `(a_n, a_n+M]` ⟺ residue in `U`, *then* `a_{n+T}=a_n+L` for `n ≥ N₀`. Proof via the
  **cyclic-successor bijection on `U`** (gives pure periodicity of residues + constant
  displacement `L`, a multiple of `K`). This is the correct, `M`-free endgame.

## The corrected crux (for next round)
`S = primes(L)` is finite but **NOT** `⊆ {p ≤ M}`. Split:
- **GAP-A (finite alphabet):** `primes(L)` is finite — the SAME crux as
  `redundant-constraint-antichain`'s Crux Lemma 1. The two surviving approaches
  **collapse onto this one gap** once the `M`-threshold is dropped. (Diversity
  warning the reviewer already flagged is now concrete: both live approaches share
  this wall.)
- **GAP-B:** after `N₀`, no new prime outside `S` becomes a sole witness (constraints
  stabilise to a fixed condition mod `K`).
- Secondary: extending periodicity from `n ≥ N₀` down to `n = 1` (backward
  determinism) — standard but nontrivial, not attempted.

## Recommendation to orchestrator/outliner
- **Retire the `M`-threshold entirely** across the field; delete the confinement
  lemma from the shared "free lemmas" list (it is false). Do NOT let any approach
  import it.
- The field has now genuinely collapsed to ONE crux (finiteness of `primes(L)` /
  finite minimal-support alphabet) with no `≤M` handle. Per CLAUDE.md's
  plateau-breaker rule, **seed a genuinely different framing next round** that does
  not route through a fixed modulus or an `M`/`K` threshold at all — e.g. a
  minimal-counterexample / infinite-descent on the least newly-recruited structural
  prime, or a growth-vs-density counting argument that bounds how many distinct
  primes can ever enter minimal supports (this is where `375`'s `19` must be
  explained: why can't ever-larger structural primes keep getting recruited?).
- Keep the proved free lemmas + Reduction Lemma as certified shared infrastructure.

## Files
- Approach file (updated): /home/agentuser/repo/results/imo-2026-06/approaches/anomaly-count-terminates.md
- Counterexample is reproducible: greedy build of `a_1=375`, factor `L=3990=2·3·5·7·19`, `M=15`.
