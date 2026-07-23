# Lemma FOM (First-Occurrence Minimality), Fan-Size Corollary, Generation-Chain Lemma

**Source.** `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`
(round 6), independently reproved inline (identical content) by
`results/imo-2026-06/approaches/core-depth-induction.md` (round 6, Lemma B1's
proof).

## Setup

For a nonempty finite set of primes `C`, define
`T_C := min{x ∈ ℤ : x > a_1, rad(x) = C}`. This is well-defined: for every
`t ≥ 1`, `(∏_{p∈C} p)^t` has radical exactly `C`, and these values are
unbounded as `t→∞`, so `{x>a_1 : rad(x)=C}` is nonempty, hence has a minimum
by well-ordering.

## Lemma FOM (First-Occurrence Minimality)

**Statement.** If `n≥2` is the first index with `rad(a_n)=C` (no `i<n` has
`rad(a_i)=C`), then `a_n = T_C`.

**Proof.** Admissibility of a candidate integer against a fixed prefix
`a_1,…,a_m` depends only on its radical (via `gcd(x,y)>1 ⟺ rad(x)∩rad(y)≠∅`),
not its magnitude.

Suppose, for contradiction, `a_n ≠ T_C`. Since `rad(a_n)=C` and `a_n` is
itself in the set `T_C` minimizes, `T_C ≤ a_n`; combined with `T_C≠a_n`,
`T_C < a_n` strictly.

*Sub-claim: `T_C` is not equal to any `a_i`, `i≥1`.* For `i≥n`: `a_i≥a_n>T_C`
(strict monotonicity), so `T_C≠a_i`. For `i<n`: if `T_C=a_i`, then
`rad(a_i)=rad(T_C)=C`, contradicting that `n` is `C`'s first occurrence. So
`T_C≠a_i` for all `i≥1`.

Since `(a_i)` is strictly increasing and unbounded, and `T_C` is a fixed
integer not equal to any `a_i`, the set `{i≥1 : a_i<T_C}` is finite and
nonempty (`a_1<T_C`). Let `i* := |{i≥1 : a_i<T_C}|`; then `a_{i*}<T_C`, and
since `T_C` is not a term, `a_{i*+1}` (the smallest term `≥T_C`) satisfies
`a_{i*+1}>T_C` strictly. Since `T_C<a_n` and `(a_i)` is increasing,
`a_{i*}<T_C<a_n` forces `i*≤n-1`.

For every `i≤i*`: since `a_n` is admissible against every `a_j`, `j<n`
(greedy rule), in particular for `j≤i*`, `rad(a_n)∩rad(a_i) = C∩rad(a_i)≠∅`;
since `rad(T_C)=C`, the same nonempty intersection shows `T_C` is admissible
against `a_1,…,a_{i*}`. By the greedy rule, `a_{i*+1}` is the smallest integer
`>a_{i*}` admissible against `a_1,…,a_{i*}`; since `T_C>a_{i*}` and `T_C` is
admissible, minimality gives `a_{i*+1}≤T_C`. Combined with `T_C<a_{i*+1}`
(shown above): `a_{i*+1}≤T_C<a_{i*+1}`, a contradiction.

Hence `a_n=T_C`. ∎

**Independent verification (proof-reviewer, round 6, fresh code, not reused
from any builder script).** Simulated the full sequence for `a_1=247,2747`
to `n=6000` (exact `sympy.factorint`-based radical computation) and checked
Lemma FOM against **every** first-occurrence index found (2106 checks for
`a_1=247`, 2817 for `a_1=2747`, via an independent heap-based smooth-number
search for `T_C`): **zero violations.**

## Fan-Size Corollary

**Statement.** Let `C'` be a nonempty finite set of primes first occurring at
index `m≥2` (so `a_m=T_{C'}` by Lemma FOM). Suppose some index `i<m` has
`rad(a_i)=C'∪{q}` for a prime `q∉C'`. Then `q·∏(C') ≤ a_i < a_m=T_{C'}`, i.e.
`q < T_{C'}/∏(C')`.

**Proof.** Since `rad(a_i)=C'∪{q}`, every prime of `C'` and `q` divide `a_i`;
as `q∉C'`, `q` and `∏(C')` are coprime, so `q·∏(C')` divides `a_i`, giving
`q·∏(C') ≤ a_i`. Since `i<m` and `(a_n)` is strictly increasing, `a_i<a_m=T_{C'}`.
Combining gives the claim. ∎

*Caution (do not overclaim).* This bound is **conditional** on `C'` actually
being realized at some future index `m` — it does not, by itself, establish
that `C'` is ever realized, nor bound (i) how many distinct absorbing values a
channel cycles through, nor (ii) whether growth could continue forever without
absorption.

## Generation-Chain Lemma

**Statement.** Fix a proper core `S⊊P_1`. Call
`C_1⊋C_2⊋⋯⊋C_r⊇S` (`r≥1`) a *domination chain in `S`* if each `C_{l+1}` is a
dominating witness (in the sense of the already-certified No-Resurrection
Lemma, `lemmas/theorem-V-veto-finite-iff-MRS.md`) that permanently excludes
`C_l` from the antichain from some point on. Then `r ≤ |C_1|-|S|+1`; in
particular every domination chain is finite.

**Proof.** `C_l⊇C_r⊇S` for every `1≤l≤r` (transitivity of `⊇`), so
`|C_l|≥|S|` for every `l`. Combined with the strict decrease
`|C_1|>|C_2|>⋯>|C_r|`, this is a strictly decreasing sequence of `r` integers
in `{|S|,…,|C_1|}` (an interval of `|C_1|-|S|+1` integers), so
`r≤|C_1|-|S|+1`. ∎

*(Chain LENGTH is not new difficulty — a three-line consequence of
No-Resurrection. The open content is chain/companion COUNT, addressed, not
closed, by the Λ_S-Reduction/Single-Companion Finiteness machinery in
`lemmas/lemma-lambda-S-reduction-and-single-companion-finiteness.md`.)*

## Certification

All three statements (Lemma FOM, Fan-Size Corollary, Generation-Chain Lemma)
independently re-derived by the round-6 proof-reviewer from scratch (matching
both the round-6 outline-reviewer's independent re-derivation and
`core-depth-induction`'s independent inline reproof) and re-verified
numerically with fresh code. No gap found. Certified `solved`-quality.
