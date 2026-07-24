## Lemmas: Parity Witness and k=0-Window Criterion for `a_1 = 3q` (CERTIFIED,
round 20)

**Source.** `a1-3q-subfamily-theorem`, round 20. Independently re-derived
(algebra) and re-verified (Python) by the round-20 proof-reviewer: exact
sequence match against the predicted `a_i = 3(q+i-1)` pattern for all primes
`q ∈ [7,120)`, `q ≠ 5`, out to 300 terms each, plus direct simulation
confirmation of the two named exceptions (`q=7`, witness `i=2`; `q=11`,
witness `i=3`) and the `q=5` exclusion.

**Setting.** `a_1 = 3q`, `q` an odd prime, `q ≠ 3`. Strong-induction
hypothesis at step `n`: `a_i = 3(q+i-1)` for `i = 1,…,n` (so `3 | a_i` for
all such `i`).

### Lemma 1 (Parity Witness)

**Statement.** If `n` is odd, then `i = n` witnesses the illegality of
`a_n+2` (i.e. `gcd(a_n+2, a_n) = 1`), independent of whether `q | (a_n+2)`.

**Proof.** Set `N := a_n+2`. `gcd(N,a_n) = gcd(N, N-a_n) = gcd(N,2)`. Since
`N = 3(q+n)-1` and `3(q+n)` has the same parity as `q+n`, `N` is odd iff
`q+n` is even; as `q` is an odd prime, this holds iff `n` is odd. So for `n`
odd, `N` is odd, `gcd(N,2)=1`, hence `gcd(N,a_n)=1`. ∎ Self-contained; uses
only `gcd(x,y)=gcd(x,x-y)` and a parity check.

**Reviewer verification.** Re-derived algebraically from scratch (identical
argument reproduced independently); spot-checked numerically that for every
odd `n` tested (`q=7,11,13,17,19,23,...`), the sequence's actual `a_n+2` is
indeed illegal via index `n` — consistent throughout.

### Lemma 2 (k=0-Window Criterion, exact resolution)

**Statement.** The first Case-(b) occurrence `n_0` (least `n` with
`q | (a_n+2)`, equivalently `q | (3n-1)`) satisfies `n_0 = (q+1)/3` if
`q ≡ 2 (mod 3)`, or `n_0 = (2q+1)/3` if `q ≡ 1 (mod 3)`, with
`K_0 := (a_{n_0}+2)/q ∈ {4,5}` respectively (`4` in the first case, `5` in
the second). The "window ≥ K_0" sufficiency criterion (a full residue system
mod `K_0` inside the available witness window `i=2,…,n_0` gives a witness
coprime to `K_0`, hence to `a_n+2 = qK_0`) holds for every prime `q ≥ 7`,
`q ≠ 5`, **except** `q=7` and `q=11`. Both exceptions are directly resolved
by hand: `q=7, n_0=5`: `a_5+2=35=7·5`; witness `i=2` (`gcd(5,8)=1`). `q=11,
n_0=4`: `a_4+2=44=11·4`; witness `i=3` (`gcd(4,13)=1`).

**Proof.** Direct computation (elementary case split on `q mod 3`, since
`3` is invertible mod `q`); threshold comparison `n_0 - 1 ≥ K_0` reduces to
`q ≥ 17` (for `q≡2 mod 3`) or `q ≥ 10` (for `q≡1 mod 3`), isolating `q=11`
and `q=7` respectively as the sole exceptions among primes `≥7`, `≠5`, both
resolved by direct hand computation as above.

**Reviewer verification.** Independently re-derived the `n_0, K_0` closed
forms and re-checked via exhaustive computation over primes `q ∈ [7,80)` —
confirmed the *only* two exceptions to the naive window-sufficiency
criterion are exactly `q=7` and `q=11`, matching the builder's claim exactly.
(Note: an unrelated, later intermediate inequality in the approach file's
open-gap discussion of the `k≥1` case contains a minor arithmetic slip — the
threshold constant `(3q-1)/(q-3)` should read `(3q+2)/(q-3)` — but this does
not affect the conclusion drawn there (`K ≥ 7` still exceeds both the
correct and the stated threshold for all `q ≥ 7`), and does not appear in
either lemma statement certified here.)

**Status.** Both lemmas correct, complete, unconditional (within their
stated `a_1=3q` setting and inductive hypothesis). Neither alone closes the
full `a_1=3q` periodicity theorem — the "Case (b), `n` even, `k≥1`" case
remains open (see `a1-3q-subfamily-theorem.md`) — but both are reusable
self-contained tools for any future round attacking this or a structurally
similar `|Q|=2` odd-seed subfamily.
