## Lemma: Constrained Singleton Coherence Lemma, with Composite-Exclusion
and Prime-Power Coherence Corollaries (CERTIFIED, round 20)

**Source.** `triangle-consistency-pigeonhole`, round 20, §6.1. Independently
re-derived from scratch by the round-20 proof-reviewer (elementary
unique-factorization argument, re-checked line by line).

**Depends on (certified).** `confined-gcd-lemma.md` (confinement of gcd
values to a fixed witness's out-of-core prime set); `double-witness-nested-
pigeonhole.md` (existence of the infinite constant-gcd class `(d*,X_B^{(0)})`
this lemma starts from — only its first pass is needed here).

**Setup.** Fix a rogue pair `(A,B)` at core `S_0`, a witness `m_A ∈ X_A`.
Pigeonholing `gcd(a_{m_A}, a_x)` over `x ∈ X_B` (infinite pigeonhole on the
finite divisor set of the fixed integer `a_{m_A}`) gives an integer
`d* = gcd(a_{m_A}, a_x)` (constant, `> 1`) and an infinite `X_B^{(0)} ⊆ X_B`
on which this holds, with every prime factor of `d*` confined to
`F'_{m_A} := P(a_{m_A}) \ S_0` (Confined-GCD Lemma).

**Statement.** Suppose some `x ∈ X_B^{(0)}` is itself a *singleton*
occurrence, i.e. `P(a_x) \ S_0 = {q_x}` for a single prime `q_x`. Then
`d* = q_x^j` for some `j ≥ 1` — in particular `d*` is a prime power, and its
prime is exactly `q_x`.

**Proof.** `d* = gcd(a_{m_A}, a_x) | a_x`. Split `a_x`'s factorization into
its `S_0`-part and its outside-core part; by the singleton hypothesis the
outside-core part is a pure `q_x`-power. Every prime factor of `d*` lies
outside `S_0` (confinement, from Confined-GCD via the Double-Witness Nested
Pigeonhole construction), so every prime factor of `d*` is a prime factor of
`a_x` lying outside `S_0` — hence equals `q_x`, the only such prime. A
positive integer all of whose prime factors equal a single fixed prime `q_x`
is `q_x^j`, `j ≥ 1` (`j ≥ 1` since `d* > 1`). ∎

**Corollary (Composite-Exclusion).** If `d*` has ≥ 2 distinct prime factors
(not a prime power), then `X_B^{(0)}` contains zero singleton occurrences of
`B` — direct contrapositive.

**Corollary (Prime-Power Coherence).** If `d* = q^k` for a single prime `q`,
then any singleton occurrence `x ∈ X_B^{(0)}` (if one exists) automatically
has `q_x = q` — direct from unique factorization applied to the two
prime-power expressions for `d*`.

**Verification.** Reviewer independently re-derived the elementary
divisibility/unique-factorization argument from scratch; it is a direct,
short consequence of Confined-GCD plus unique factorization, with no
dependence on any open hypothesis.

**Scope note.** This lemma is a *search-pruning tool*, not a resolution of
the existence question "does some `m_A` induce a prime-power `d*` with a
matching singleton `x`?" — the round-20 approach file independently shows
(§6.2–§6.4, not separately certified, diagnostic content) that the positive
computational evidence for that existence question on the workspace's only
two known hard test seeds is a confound (both seeds already have their
Cofinite-FAH witness established by an unrelated mechanism, the Two-Sided
Singleton Witness Theorem), so this lemma should NOT be cited as evidence
toward closing H1 in general.

**Status.** Correct, complete, unconditional. Reusable by any future
approach that pigeonholes a gcd value against a fixed witness and wants to
know what a co-occurring singleton implies about the pigeonholed value (or
vice versa).
