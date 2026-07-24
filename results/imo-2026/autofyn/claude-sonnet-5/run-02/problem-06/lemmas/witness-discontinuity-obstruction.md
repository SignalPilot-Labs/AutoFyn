## Witness Discontinuity Obstruction — CERTIFIED, round 7

**Source.** `scalar-well-ordering-lock-in`, round 7.

**Depends on.** Only the greedy defining rule and elementary factorization; uses the
recruitment-process machinery (Extended Persistent-Type Pigeonhole, Lemma G) only to
set up the example, not in the proof of the existence claim itself.

**Statement.** There exist a finite S₀ ⊇ Q, a persistent base type B, an
S₀-extended-persistent refinement B' of B with earliest witness index
m := min{n : ρ_{S₀}(n) = B'}, and a prime q | a_m with q ∉ S₀, such that — setting
S₁ := S₀ ∪ {q} and letting B'' be the S₁-refinement of B agreeing with B' on S₀ and
excluding q (forced since q ∉ B' ⊆ S₀) — the earliest S₁-witness m' of B''
satisfies m' ≠ m and q ∤ a_{m'}. In words: enlarging the core by the very prime
recruited against a type can push that type's earliest witness to a *later* index
whose value happens not to carry the recruited prime.

**Explicit witnessing example (a_1 = 175).** a_1=175, a_2=180=2²·3²·5,
a_3=182=2·7·13, a_4=189=3³·7 (verified by direct factorization and the greedy
legality/minimality rule). Take S₀ = {5,7} = Q, B = B' = {7}: ρ_{S₀}(3) =
P(182)∩{5,7} = {7}, and this is the earliest occurrence, so m = 3. Take q = 2 (a
prime dividing a_3 = 182 but not in S₀). S₁ = {2,5,7}: ρ_{S₁}(3) = P(182)∩{2,5,7} =
{2,7} ≠ {7}, so index 3 no longer witnesses the "pure {7}" type B'' at level S₁; the
next occurrence of ρ_{S₁}(n) = {7} exactly is n = 4 (ρ_{S₁}(4) = P(189)∩{2,5,7} =
{7}, since 189 = 3³·7 is odd), giving m' = 4 ≠ m = 3 and q = 2 ∤ a_4 = 189. ∎

**Proof of existence.** The example above is fully exhibited and directly verified
by hand (elementary factorization of four small integers), so existence follows
immediately; no further argument is needed beyond checking the arithmetic.

**Scope.** A genuine, unconditional, reusable negative fact about the extended-type
machinery: "the earliest witness of a fixed extended-persistent type" is NOT
continuous/stable under enlarging the core S₀ by a prime recruited against that very
witness. In particular, no algebraic recursion tracking a scalar quantity defined
via "the current earliest witness" across successive recruitment stages can assume
the recruited prime persists into the next stage's witness — this rules out, in
general (not just for one example), any proof mechanism for FAH/Symmetric FAH built
on such a continuity assumption. Unlike the workspace's non-certified diagnostic
Lemma I/Lemma F (which are meta-statements about what the *current* certified
toolkit can compose), this is a direct existence claim about the greedy sequence and
the extended-type construction themselves, true regardless of what else is proved or
certified later.

**Status.** Correct, complete, no gaps, unconditional. Certified by the round-7
proof-reviewer: independently regenerated the sequence a_1=175 by direct
trial-division simulation and reconfirmed a_1..a_4 = 175, 180, 182, 189 exactly,
and reconfirmed ρ_{S₀}(3), ρ_{S₁}(3), ρ_{S₁}(4) as claimed — no gap.
