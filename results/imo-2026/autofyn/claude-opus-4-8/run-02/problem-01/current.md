# imo-2026-01 — Confucius's gcd/lcm blackboard

## Status
solved

## Approaches tried
- **perprime-valuation** — worked (APPROVE, round 1). Per-prime valuation decomposition: the move is
  one subtractive-Euclid step `(a,b)↦(min(a,b),|a-b|)` on each prime; lex monovariant `(Ω_tot,C)` gives
  termination; `g_p=gcd_i v_p(x_i)` is invariant, giving both parts and the closed form `M=∏_p p^{g_p}`.
  Self-contained, cleanest route. Adopted as the Full proof below.
- **descent-induction** — worked (APPROVE, round 1). Same three lemmas; part (b) obtained instead by
  well-founded (minimal-counterexample) descent on `(Ω_tot,C)`, with the share-one-cell critical pair
  closed by an EXPLICIT common reduct `{s,1,1}` (s=∏ p^{gcd(v_p x,v_p y,v_p z)}) built from the g_p
  invariant — verified non-circular. A second independent complete proof.

## Current best
Full proof below (both parts complete and rigorous).

## Full proof

### Setup and conventions
The board is a multiset of `N=2026` positive integers `(x_1,…,x_N)`, initially all `>1`; position
labels are bookkeeping only (the board is unordered). A move is legal iff ≥2 entries exceed 1; it picks
`i≠j` with `x_i=m>1`, `x_j=n>1` and replaces them by `gcd(m,n)` and `lcm(m,n)/gcd(m,n)`.

`lcm(m,n)/gcd(m,n)` is a positive integer: `lcm(m,n)=mn/gcd(m,n)` and `gcd(m,n)|m`, so
`gcd(m,n)|lcm(m,n)`. For a prime p and positive integer x, `v_p(x)` is the exponent of p; by unique
factorization `v_p(gcd(m,n))=min(v_p m,v_p n)`, `v_p(lcm(m,n))=max(v_p m,v_p n)`, and `v_p(m/n)=v_p m−v_p n`
when `n|m`. Integer gcd uses `gcd(a,0)=a`, `gcd(0,0)=0`; gcd of a finite list is well-defined (associative,
commutative on ℕ). `Ω(x)=Σ_p v_p(x)`. Only finitely many primes ever occur, so all products/sums over p
are finite.

### Lemma 1 (per-prime move law)
For a move on `m,n` producing `d=gcd(m,n)`, `e=lcm(m,n)/gcd(m,n)`, every prime p with `a=v_p m,b=v_p n`:
`v_p(d)=min(a,b)`, `v_p(e)=v_p(lcm)−v_p(gcd)=max(a,b)−min(a,b)=|a−b|`. Thus the touched valuation pair
transforms `{a,b}↦{min(a,b),|a−b|}`; untouched positions are unchanged. (v_p=0 for both ⇒ {0,0}↦{0,0}.)

### Lemma 2 (termination via lex monovariant)
Let `Ω_tot=Σ_i Ω(x_i)` and `C=#{i:x_i>1}`, ordered lexicographically on ℕ×ℕ. For a move:
`ΔΩ_tot = Σ_p(max(a_p,b_p)−a_p−b_p) = −Σ_p min(a_p,b_p) = −Ω(gcd(m,n)) ≤ 0`.
- If `gcd(m,n)>1`: `Ω(gcd)≥1`, so `Ω_tot` strictly drops ⇒ `(Ω_tot,C)` drops.
- If `gcd(m,n)=1`: `Ω_tot` unchanged; here `e=mn>1` and `{m,n}→{1,mn}`, so the two cells go from two
  values `>1` to exactly one, `C` drops by exactly 1 ⇒ `(Ω_tot,C)` drops.
So every move strictly decreases `(Ω_tot,C)`. Lex order on ℕ×ℕ is a well-order (first coordinates
non-increasing hence eventually constant, then second strictly decreasing — impossible forever), so every
maximal move sequence is finite. It halts only when no legal move exists, i.e. `C≤1`.

### Lemma 3 (per-prime gcd invariant)
For all `a,b≥0`: `gcd(min(a,b),|a−b|)=gcd(a,b)`. (WLOG `a≤b`: `gcd(a,b−a)=gcd(a,b)` by subtractive
Euclid; edge cases `a=b⇒gcd(a,0)=a`, `a=0⇒gcd(0,b)=b`.) Also, replacing two list entries `a,b` by
`gcd(a,b)` preserves the list's overall gcd (an integer divides both a,b iff it divides gcd(a,b)).
Hence for `g_p=gcd(v_p(x_1),…,v_p(x_N))`, a move (which sends the two touched coordinates
`{a,b}↦{min(a,b),|a−b|}`, others fixed) gives, with `R` the untouched coordinates:
`g_p(after)=gcd(R,min(a,b),|a−b|)=gcd(R,gcd(min,|a−b|))=gcd(R,gcd(a,b))=gcd(R,a,b)=g_p(before)`.
So each `g_p` is invariant under every move, equal always to its initial value
`gcd(v_p(x_1^init),…,v_p(x_N^init))`.

### Part (a): exactly one survivor
By Lemma 2 the process halts with `C≤1`. Some initial entry is `>1`, hence divisible by some prime p, so
`v_p(x_i^init)≥1` for some i; then `g_p^init=gcd(…)≥1`. By invariance `g_p≥1` at the halt. If the halt had
all entries `=1`, every valuation would be 0 and `g_p=0` — contradiction. So `C≥1`. With `C≤1`, exactly
`C=1`: precisely one entry `M>1` survives. ∎

### Part (b): value of M is choice-independent
At the halt the multiset is `{M,1,…,1}`, so for each prime p, `g_p=gcd(v_p(M),0,…,0)=v_p(M)`. By Lemma 3
this equals the initial `gcd(v_p(x_1^init),…,v_p(x_N^init))`, which depends only on the starting board.
Hence for every prime p, `v_p(M)=gcd_i v_p(x_i^init)`, and by unique factorization
```
M = ∏_p p^{ gcd_i v_p(x_i^init) },
```
a finite product with `M>1` (some `g_p≥1`). This value is determined solely by the initial multiset, so
`M` is the same for every valid sequence of moves. ∎

### Verification
`{4,8,3}`: `g_2=gcd(2,3,0)=1`, `g_3=gcd(0,0,1)=1` ⇒ `M=6`. Two different plays both terminate at
`{6,1,1}`. A simulation over 3000 random boards, each played to completion in 15 random move-orders,
confirmed the survivor is always unique and equals `∏_p p^{g_p}`; the per-prime move law and the identity
`gcd(min(a,b),|a−b|)=gcd(a,b)` were checked exhaustively.

## Independent second proof (descent-induction)
An alternative complete proof (approaches/descent-induction.md) derives part (b) by well-founded induction
on `(Ω_tot,C)`: every maximal sequence from a board ends at the same terminal board. The only nontrivial
critical pair (two first moves sharing one cell) is joined by the explicit common reduct `{s,1,1}` on the
three cells, `s=∏_p p^{gcd(v_p x,v_p y,v_p z)}`, certified by the `g_p` invariant (Lemma 3) — not by
"normal forms are unique," so non-circular. Both proofs are correct.
