# Lemma ERD / RBD (Realized–Blocked Dichotomy for radical classes)

**Source.** Proved independently, this round (round 8), by two builders as
two differently-named but identical statements: `sunflower-bundle-closure.md`
(as **Lemma ERD-C**, §1) and `persistent-backbone-monovariant.md` (as the
**Realized–Blocked Dichotomy Lemma (RBD)**, in "Round 8: Realized–Blocked
Dichotomy..."). Both proofs use the identical mechanism (already-certified
Lemma ER, Lemma P′, Permanent-Inadmissibility Lemma) and prove the identical
statement about the identical object (an arbitrary nonempty finite set of
primes). Merged into one certified lemma file per this workspace's standing
convention (see `theorem-V-veto-finite-iff-MRS.md` for precedent).

## Statement

Let `κ` be any nonempty finite set of primes. Exactly one of the following
holds:

(i) **`κ` is realized**: `∃` a finite index `m≥1` with `rad(a_m)=κ`.

(ii) **`κ` is blocked**: `∃` a finite index `j≥1` with `rad(a_j)∩κ=∅`; and
then `κ` is never realized at any index.

## Proof

*Well-definedness of a canonical test integer.* Let `T_κ:=min{x>a_1:
rad(x)=κ}`. For any `t≥1`, `(∏_{p∈κ}p)^t` has radical exactly `κ` and these
values are unbounded as `t→∞`, so the minimizing set is nonempty and `T_κ` is
well-defined by well-ordering; `T_κ>a_1` by construction.

*Mutually exclusive.* Suppose `κ` is realized at index `n` (`rad(a_n)=κ`)
and blocked by witness `j` (`rad(a_j)∩κ=∅`). If `n≠j`, the already-certified
Lemma P′ gives `gcd(a_n,a_j)>1`, i.e. `rad(a_n)∩rad(a_j)=κ∩rad(a_j)≠∅`,
contradicting the blocking hypothesis. If `n=j`, the blocking hypothesis
directly gives `κ∩κ=∅`, i.e. `κ=∅`, contradicting nonemptiness. Either way,
contradiction.

*Exhaustive.* Suppose `κ` is not blocked: `rad(a_j)∩κ≠∅` for every `j≥1`.
Then `gcd(T_κ,a_j)>1` for every `j` (a common prime `p∈κ∩rad(a_j)` divides
both `T_κ`, since `rad(T_κ)=κ`, and `a_j`). Since `T_κ>a_1`, the
already-certified Lemma ER (contrapositive form) applies directly to
`y:=T_κ`: either `T_κ=a_m` for some `m` (giving `rad(a_m)=κ`, i.e. `κ`
realized), or the hypothesis of Lemma ER is contradicted — but the hypothesis
(`y>a_1`, `gcd(y,a_i)>1` for all `i`) is exactly what was just shown, so
Lemma ER forces `T_κ=a_m` for some `m`. Hence `κ` is realized.

*"Never realized" clause of (ii).* Shown as a byproduct of the
mutual-exclusion argument: if `κ` is blocked by `j`, no index `n` (whether
`n=j`, `n<j`, or `n>j`) can have `rad(a_n)=κ`, by the same contradiction
argument (using Lemma P′ for `n≠j`, direct nonemptiness for `n=j`), applied
uniformly to every candidate `n`, not just a single fixed one. `∎`

## Certification

Fully proved, general-purpose (holds for any proper core, or indeed any
nonempty finite prime set, of any sequence satisfying this problem's
hypotheses). No circularity: depends only on the already-certified Lemma ER,
Lemma P′, and the Permanent-Inadmissibility Lemma. Independently re-verified
by the round-8 proof-reviewer (re-derived from scratch, confirmed both
source proofs are the identical argument up to notation). Certified
`solved`-quality.

**Independent verification (proof-reviewer, round 8).** Re-derived the full
proof from scratch, hand-checked both mutual-exclusion cases and the
exhaustiveness direction; confirmed no gap. Independently reproduced, via
fresh Python (own greedy-sequence generator, cross-validated against
brute-force on 5 small `a_1` before trusting larger runs), the worked
instance `a_1=2747,S={67}` cited by `persistent-backbone-monovariant`'s
round-8 worked example: `a_1=2747` (rad `{41,67}`), `a_2=2788` (rad
`{2,17,41}`), `a_3=2814` (rad `{2,3,7,67}`), `a_4=2829` (rad `{3,23,41}`),
`a_10=3157` (rad `{7,11,41}`) — exact match, confirming `S={67}` is blocked
by `j=2` as claimed.
