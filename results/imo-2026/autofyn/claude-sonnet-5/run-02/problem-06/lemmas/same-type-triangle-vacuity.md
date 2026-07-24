## Lemma: Same-Type Triangle Vacuity (CERTIFIED, round 19 — content from round 18)

**Source.** `triangle-consistency-pigeonhole`, round 18, §2. Independently
re-verified by the round-19 proof-reviewer.

**Depends on (certified).** `free-facts-gcd.md`; `same-type-free-facts-
vacuity.md` (the general phenomenon this instantiates for the specific
"triangle" quantity `e`); `confined-gcd-lemma.md` (to note it does not help
here).

**Setup.** Fix a rogue pair `(A,B)` at core `S_0`, and two distinct
occurrences `m_A, m_A'` of the SAME type `A` (`ρ(m_A)=ρ(m_A')=A`). Let
`e := gcd(a_{m_A}, a_{m_A'})`, and `F'_{m_A} := P(a_{m_A})\S_0`,
`F'_{m_A'} := P(a_{m_A'})\S_0` (the two witnesses' fixed out-of-core prime
sets, as in the Double-Witness Nested Pigeonhole Lemma).

**Statement.** `e` carries no information about `F'_{m_A} ∩ F'_{m_A'}`: Free
Facts' conclusion `e>1` is already fully explained by the in-core primes of
`A` alone (`A ⊆ P(a_{m_A}) ∩ P(a_{m_A'})`, so `∏_{p∈A} p^{min(v_p(a_{m_A}),
v_p(a_{m_A'}))} | e`), and no certified tool (Confined-GCD or otherwise)
forces any outside-core factor of `e`, if one exists, to lie in
`F'_{m_A} ∩ F'_{m_A'}` specifically.

**Proof.** Since `A` is nonempty (any persistent type is, by the Preliminary
Fact that every extended type is nonempty) and `A ⊆ P(a_{m_A}) ∩ P(a_{m_A'})`
by definition of type, the stated product divides `e`, so `e>1` needs no
input beyond `A`'s own in-core primes — this is `same-type-free-facts-
vacuity.md`'s phenomenon applied to the specific quantity `e`. Confined-GCD's
confinement mechanism (used in the Double-Witness lemma) requires a
*disjoint*-type partner to rule out in-core primes as an explanation; here
both witnesses share the *same* type `A`, so that mechanism supplies nothing.
Hence `e`'s out-of-core part (if any) is logically unconstrained by the
certified toolkit: it need not exist, and even if it does, it need not meet
`F'_{m_A} ∩ F'_{m_A'}`. ∎

**Scope note (independently confirmed by this review, not merely asserted).**
This is a genuine negative result about the specific "triangle" construction
`e := gcd(a_{m_A}, a_{m_A'})` applied to two SAME-type witnesses — it kills
this construction as a route to forcing a shared out-of-core prime across
disjoint-type witness pairs. It does **not** by itself rule out every
possible multi-witness mechanism (e.g. it does not touch the Two-Sided
Singleton Witness Theorem, which uses no such same-type triangle at all).

**Status.** Correct, complete, unconditional. Reusable diagnostic: any future
attempt to extract cross-witness linking information from a same-type pair's
gcd should be checked against this Lemma first.
