# Certified lemmas: per-prime Euclidean-step identities (imo-2026-01)

Certified by proof-reviewer, round 1, from `induction-on-active-count.md` (Section 0
and Lemma SM/Lemma GP proofs). All are `sorry`-free, self-contained, and independently
re-verified (including by direct numerical check) by the reviewer.

## Lemma I1 (monovariant inequality)
For nonnegative integers `a,b`,
$$\min(a,b)^2 + |a-b|^2 \;\le\; a^2+b^2,$$
with equality if and only if `\min(a,b)=0`.

*Proof.* WLOG `a\le b`. Then `\min(a,b)=a`, `|a-b|=b-a`, and
`a^2+b^2-(a^2+(b-a)^2) = b^2-(b-a)^2 = a(2b-a) \ge 0` since `0\le a\le b` implies
`2b-a\ge a\ge0`. Equality iff `a(2b-a)=0` iff `a=0` (since `a=2b` together with
`a\le b` forces `a=b=0` too). $\blacksquare$

## Lemma I2 (gcd invariance under one Euclidean step)
For nonnegative integers `a,b` (convention `\gcd(x,0)=x`, `\gcd(0,0)=0`),
$$\gcd(\min(a,b),|a-b|) = \gcd(a,b).$$

*Proof.* If `a=b` both sides equal `a`. Otherwise WLOG `a<b`: `d\mid a,b \iff d\mid a,
b-a`, so `\{a,b\}` and `\{a,b-a\}` have identical common-divisor sets, hence the same
gcd. $\blacksquare$

## Lemma L1 (not both trivial)
If `m,n>1` are integers, `g=\gcd(m,n)` and `q=\operatorname{lcm}(m,n)/\gcd(m,n)` are
not both equal to `1`.

*Proof.* By definition `g\cdot q = \operatorname{lcm}(m,n)` (immediate: `q` is defined
as `\operatorname{lcm}(m,n)/g`, so `gq=\operatorname{lcm}(m,n)` directly, with no need
for the separate identity `\gcd(m,n)\cdot\operatorname{lcm}(m,n)=mn`). Since `m` divides
`\operatorname{lcm}(m,n)`, `\operatorname{lcm}(m,n)\ge m>1`, so `gq>1`, impossible if
`g=q=1`. $\blacksquare$

**Caution (documented pitfall):** `g\cdot q = \operatorname{lcm}(m,n)`, **not** `mn`.
The identity `\gcd(m,n)\cdot\operatorname{lcm}(m,n)=mn` is a *different, true* fact but
does not give `gq=mn` (that would require `g\cdot\operatorname{lcm}(m,n)=mn`, not
`g\cdot q`). Numerically, `m=4,n=6`: `g=2,q=6`, `gq=12=\operatorname{lcm}(4,6)`, while
`mn=24\ne 12`. An earlier draft (`lex-potential-gcd-invariant.md`) asserted `gq=mn`
as a "standard identity" — this is false in general; use the direct one-line
argument above instead.

## Lemma SM (Single-Move Lemma)
Let `B` be a board (multiset of positive integers at fixed positions) with
`k(B)\ge2` active (`>1`) entries, and `B'` obtained by one legal move (replacing two
active entries `m,n` by `g=\gcd(m,n)`, `q=\operatorname{lcm}(m,n)/\gcd(m,n)`). Exactly
one of:
- (Drop) `k(B')=k(B)-1`, or
- (Stall) `k(B')=k(B)` and `\Sigma(B')<\Sigma(B)`, where
  `\Sigma(B)=\sum_i\sum_p v_p(B(i))^2`.

*Proof.* Uses I1, I2, L1 and the per-prime identity `(v_p(g),v_p(q)) =
(\min(a,b),|a-b|)` for `a=v_p(m),b=v_p(n)` (immediate from unique factorization and
`v_p(\gcd)=\min`, `v_p(\operatorname{lcm})=\max`). Full argument in
`approaches/induction-on-active-count.md`, Section 2. $\blacksquare$

## Lemma GP (`G_p`-invariance)
For every prime `p`, `G_p(B) := \gcd(v_p(B(1)),\dots,v_p(B(2026)))` is unchanged by
every legal move.

*Proof.* Via I2 and the standard fact that gcd distributes over multiset
concatenation: `\gcd(R\cup\{a,b\}) = \gcd(\gcd(R),\gcd(a,b))`. Full argument in
`approaches/induction-on-active-count.md`, Section 4. $\blacksquare$

Reusable by any approach to imo-2026-01 needing the per-prime reduction (termination
potential) or the `G_p` invariant (uniqueness of `M = \prod_p p^{G_p}`).
