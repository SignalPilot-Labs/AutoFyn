# Lemma D1 — small-discrepancy kill (general n)

**Status:** certified (proof-reviewer, round 10). Proof re-derived by the reviewer; verified over 47114
random configs with `|N_Q−N_R| ≤ 1` (0 violations).

## Statement
For finite multisets `Q, R` of positive reals with `N_P(x) := #{parts of P > x}`, if
`|N_Q(x) − N_R(x)| ≤ 1` for every `x ≥ 0`, then
```
A(Q ∪ R) ≥ |ΣQ − ΣR|.
```
In particular, in bucket (iii) of the lower-bound problem (`ΣQ = 2ⁿ`, `ΣR = 2ⁿ − 1`), `A(Q∪R) ≥ 1`.

## Proof
By additivity `N_{Q∪R} = N_Q + N_R`, and by the measure form (Lemma M0, `alt-sum-integral.md`),
`A(Q∪R) = measure{x : N_Q(x)+N_R(x) odd}`. Set `g := N_Q − N_R`. Since `(N_Q+N_R) − (N_Q−N_R) = 2N_R`
is even, `N_Q+N_R ≡ g (mod 2)`, so
```
A(Q∪R) = measure{x : g(x) odd}.
```
`g` is integer-valued with `|g| ≤ 1`, so `g(x)` is odd **iff** `g(x) ≠ 0`, and `|g| = 𝟙[g ≠ 0]`. Hence
```
A(Q∪R) = measure{g ≠ 0} = ∫ |g| dx ≥ | ∫ g dx | = |ΣQ − ΣR|,
```
using `∫₀^∞ N_P dx = Σ_{p∈P} ∫₀^p dx = ΣP` and the triangle inequality. ∎

## Scope / remarks
- Requires the pointwise smallness hypothesis `|N_Q − N_R| ≤ 1`; it does NOT apply when the discrepancy
  reaches 2 somewhere (the recorded `∫g = 1` obstruction: `g ≡ 2` on `[0,½)` integrates to 1 but is never
  odd). It is the first rigorous general-`n` GAP cheap-kill that beats that obstruction.
- Reusable by both lower-bound routes (dyadic-symdiff GAP package, inclusion-gap non-containment branch).
