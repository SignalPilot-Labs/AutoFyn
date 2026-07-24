## Status
unsolved (approach terminated this round with a definitive negative result —
recommend RETHINK/retirement of this slug; see below)

## Approaches tried

- **Round 20 (this round, first build).** Task: (1) mandatory equivalence
  check against `triangle-consistency-pigeonhole`'s existence gap, then (2)
  push the Critical Prime Dichotomy Lemma's branch (b) ("sole rescuer")
  toward the Two-Sided Singleton Witness Theorem's existence hypothesis.
  **Result: the equivalence check came back negative (the two constructions
  are genuinely different objects, confirming the outline-reviewer's
  read) — but a stronger and more decisive fact emerged first: branch (b) of
  the Critical Prime Dichotomy Lemma is UNCONDITIONALLY VACUOUS — it can
  never fire, for any n, any prime, any core. This is proved in full below
  (§B) and confirmed computationally with zero exceptions across ~2400
  seeds and thousands of (n, prime) pairs, including both known hard seeds
  `a_1=4807` and `a_1=11305` at their properly recruited cores out to
  N=2500–3000.** Since this approach's entire mechanism (Step 2 of the
  outline: invoke branch (b) to obtain a "sole rescuer" index) depends on
  branch (b) ever occurring, and it never does, the approach cannot be
  carried forward in the form proposed. This is reported as a genuine,
  fully proved negative result — not a stall — per the round's instruction
  to surface a gap honestly rather than force artificial progress.

## Current best

### §A. Mandatory equivalence check against `triangle-consistency-pigeonhole`

I compared this approach's proposed construction against the sibling's own
open existence gap (`triangle-consistency-pigeonhole.md` §4, the Two-Sided
Singleton Witness Theorem's hypothesis: existence of `x_1` with `ρ(x_1)=B`,
`P(a_{x_1})\S_0=\{q\}` singleton, and `x_2` with `ρ(x_2)=A`,
`P(a_{x_2})\S_0=\{q\}` singleton, same `q`).

This approach's proposed object (outline Step 2/3): fix a *later* occurrence
`n∈X_{A'}` and *one* outside-core prime `q'|a_n`; the Critical Prime
Dichotomy Lemma's branch (b) gives an *earlier* index `i<n` with
`P(a_i)∩P(a_n)=\{q'\}` **exactly** — a purely *local, pairwise* intersection
fact between `a_i` and `a_n`. This says nothing about `P(a_n)\S_0` as a
*whole set* — `a_n` may have other outside-core primes besides `q'`, each
individually resolved (if at all) by its own, unrelated dichotomy instance
with a possibly different earlier index. In particular, "branch (b) fires
for `q'` at `n`" does **not** imply `P(a_n)\S_0=\{q'\}` (singleton), which
is what the sibling's existence hypothesis needs on the `A`-occurrence side.
Nor does it produce anything about a `B`-occurrence at all (the rescued
index `i` need not have `ρ(i)=B` — its type is a priori unconstrained by
the dichotomy's proof, which only uses minimality of `a_n`, not `i`'s type).

**Conclusion of the equivalence check.** The two constructions are
genuinely different objects, exactly as the outline-reviewer assessed: the
sibling pigeonholes a *global* gcd value over *many later* occurrences of
the *other* type, fixed at *one* early witness of *this* type (forward,
one-witness-vs-many-candidates, producing a full divisor-class fact); this
approach looks *backward* from *one* later occurrence and *one* of its
outside-core primes to find *one* specific earlier rescued index of
*unconstrained* type (backward, one-term-vs-one-prime, producing only a
pairwise intersection fact, not a full singleton-signature fact). They do
**not** collapse into the same statement under relabeling — so this is not
a same-mechanism duplicate, and the mandatory equivalence check does *not*
by itself call for a RETHINK. (The RETHINK verdict below is instead forced
by the independent, stronger finding in §B.)

### §B. New finding: Critical Prime Dichotomy's branch (b) is unconditionally
vacuous — full proof

**Theorem (Universal Branch-(a) Dominance).** For every `n≥2`, every prime
`p` dividing `a_n`, and `e:=v_p(a_n)≥1`, `c:=a_n/p^e` satisfies `c≤a_{n-1}`.
Consequently — specializing to any finite core `S_0⊇Q` and any prime
`q'|a_n` with `q'∉S_0` — branch (a) of the Critical Prime Dichotomy Lemma
(`lemmas/critical-prime-dichotomy.md`) **always** holds, so branch (b)
**never** needs to fire and, moreover, the Lemma's proof never actually
reaches the case that produces it (the hypothesis "`¬`(a)" of its
implication `¬(a)⟹(b)` is never satisfied). This holds for *every* index
`n≥2` and *every* prime factor of `a_n` — not merely for outside-core
primes, and not merely for the two known hard seeds.

**Proof.** Fix `n≥2`, a prime `p|a_n`, `e:=v_p(a_n)≥1`, `c:=a_n/p^e`
(so `\gcd(c,p)=1` and `p^e\|a_n`).

*Step 1 (ratio bound via the Bounded Gap Lemma).* By the certified Bounded
Gap Lemma (`lemmas/bounded-gap-lemma.md`), for every `m≥1`,
`a_{m+1}\le a_m+a_1`. Applying this with `m:=n-1` (valid since `n≥2⟹m≥1`)
gives
```
a_n \le a_{n-1} + a_1.   (*)
```

*Step 2 (case n≥3: strict ratio bound).* The sequence `(a_k)` is strictly
increasing by the problem's own defining rule (`a_{k+1}` is required to
*exceed* `a_k`). Hence for `n\ge3`, `n-1\ge2>1`, so `a_{n-1}>a_1` strictly.
Substituting into `(*)`:
```
a_n \le a_{n-1}+a_1 < a_{n-1}+a_{n-1} = 2a_{n-1}.
```
So `a_n<2a_{n-1}` strictly, for every `n\ge3`.

Since `p\ge2` is prime and `e\ge1`, `p^e\ge2`. Dividing `a_n<2a_{n-1}` by
`p^e\ge2`:
```
c = a_n/p^e \le a_n/2 < a_{n-1}.
```
(The middle inequality `a_n/p^e\le a_n/2` uses `p^e\ge2`; the last uses
`a_n<2a_{n-1}` so `a_n/2<a_{n-1}`.) Hence `c<a_{n-1}`, so `c\le a_{n-1}`
holds (in fact strictly) — branch (a).

*Step 3 (case n=2: boundary, non-strict bound suffices).* Here `n-1=1`, so
`a_{n-1}=a_1` exactly, and `(*)` reads `a_2\le a_1+a_1=2a_1=2a_{n-1}`. Since
`p^e\ge2`:
```
c = a_n/p^e \le a_n/2 \le (2a_{n-1})/2 = a_{n-1}.
```
So `c\le a_{n-1}` holds (possibly with equality) — branch (a).

*Conclusion.* In every case `n\ge2`, `c\le a_{n-1}`, i.e. branch (a) of the
Critical Prime Dichotomy Lemma always holds. This is true for *every* prime
factor `p` of `a_n` (the argument used only `p\ge2`, `e\ge1`; it never used
`p\notin S_0` or any core-membership fact), so in particular it holds for
every outside-core prime `q'` of every finite core `S_0\supseteq Q`, which
is exactly the Lemma's own hypothesis class. Since the Lemma's proof
derives branch (b) *only* from the negation of branch (a) (its proof
literally begins "Suppose (a) fails"), and we have just shown (a) never
fails, branch (b) is never invoked by any legitimate instance of the
Lemma's proof machinery — it is vacuously true whenever it is asserted (the
disjunction "(a) or (b)" is always witnessed by (a) alone), and no
construction that requires *finding* a genuine branch-(b) rescuer (as this
approach's Step 2 does) can ever succeed. $\blacksquare$

**Tightness / equality case.** The bound `c\le a_{n-1}` can be an equality:
at `n=2` with `p^e=2` exactly and `a_2=2a_1` exactly (e.g. `a_1=5`, giving
`a_2=10` since `\gcd(6,5)=\gcd(7,5)=\gcd(8,5)=\gcd(9,5)=1` but
`\gcd(10,5)=5>1`; here `p=2`, `e=1`, `c=5=a_1=a_{n-1}`). This confirms the
bound is sharp — it is not slack by an accidental large margin, so the
result is not a coarse over-approximation obscuring some subtler
possibility of failure; it genuinely pins the boundary case exactly to the
`n=2`, `p^e=2` configuration, and even there branch (a) still holds
(non-strictly).

**Computational confirmation (exhaustive within tested range, zero
exceptions).**
- Both known properly-recruited-core hard seeds, at their actual recruited
  cores: `a_1=4807` (`S_0=\{2,3,5,11,19,23\}`), checked all `n` from 2 to
  3000 and every outside-core prime of every `a_n` in that range (2997
  (n, prime) instances) — branch (a) held in all 2997, branch (b) in 0.
  `a_1=11305` (`S_0=\{2,3,5,7,13,17,19,23,29,37,43,101\}`), checked `n` from
  2 to 2500 (2087 instances) — branch (a) held in all 2087, branch (b) in 0.
- Broader sweep: 1996 additional seeds `a_1\in\{4,\dots,1999\}`, each at its
  own unrecruited core `S_0=Q=P(a_1)`, each checked out to `N=800` terms —
  branch (a) held in every single (n, prime) instance encountered across
  all 1996 seeds; branch (b) never fired once.
- (Scripts preserved at `/tmp/round-20/sim_dichotomy2.py`,
  `/tmp/round-20/sim_fast.py`, `/tmp/round-20/sim_fast2.py`,
  `/tmp/round-20/sim_ratio.py`.)

This computational record is now fully *explained* (not merely observed)
by the proof above: it is not a coincidence of the two hard seeds or a
sampling artifact, but a necessary unconditional consequence of the
Bounded Gap Lemma plus strict monotonicity of `(a_n)`.

### §C. Consequence for this approach and for the Critical Prime Dichotomy
Lemma's certified write-up

1. **This approach (`triangle-critical-dichotomy-witness`) cannot be
   carried forward as outlined.** Outline Step 2 ("apply the Critical Prime
   Dichotomy Lemma: either (a)... or (b)... [branch (b), the sole rescuer]")
   presupposed that branch (b) is a genuine, occasionally-available tool to
   build on. §B shows branch (b) is *never* available — there is no
   legitimate instance to extract a rescued index `i` from, so outline
   Steps 3–4 (the "new target lemma" and "bridging step") have no object to
   act on. This is not a matter of the construction being merely hard to
   push further; the object the construction is built around does not
   exist. **Recommend RETHINK** for this slug: it should not be
   re-dispatched in its current form. (This verdict is *independent* of
   the equivalence check in §A — even though §A confirmed the two
   constructions are genuinely different, this construction individually
   fails for its own, unrelated reason.)
2. **The certified Critical Prime Dichotomy Lemma's own `Scope` paragraph
   should be revised for future rounds.** Its current text ("nothing
   prevents two distinct primes q', q'' ∈ F' from each independently
   satisfying branch (b) via different earlier witnessing indices...")
   describes a hypothetical scenario that, per §B, can never actually
   occur — branch (b) never fires for *any* prime, so this scenario is
   vacuous, not merely unexploited. The Lemma's own *statement* (an "at
   least one of (a) or (b)" disjunction) and its *proof* remain fully
   correct and are not contradicted by §B — §B merely shows the disjunction
   is always resolved by the first disjunct, a strictly stronger fact than
   the Lemma states. I flag this for the reviewer to fold into the
   certified lemma file (either as an added corollary or an updated Scope
   note) rather than editing another approach's certified lemma directly
   from this file.
3. This is now the workspace's **third** confirmed-vacuous mechanism variant
   for FAH (after Escape-Cost Vacuity and Same-Type Triangle Vacuity),
   reusable as a negative reference for future rounds: any future proposal
   that relies on the Critical Prime Dichotomy Lemma's branch (b) actually
   occurring should be screened against this result before being built.

## Full proof
Not present — Status is `unsolved`; H1/FAH is not established by this
approach, which has been shown structurally incapable of proceeding.

## Promotable lemmas

- **Universal Branch-(a) Dominance Theorem** (§B above, fully proved,
  unconditional, no dependence on core recruitment, rogue pairs, or any
  open hypothesis — depends only on the certified Bounded Gap Lemma and the
  problem's own strict-monotonicity defining rule). For every `n\ge2` and
  every prime `p\mid a_n` with `e:=v_p(a_n)`, `a_n/p^e\le a_{n-1}`.
  Consequence: branch (b) of the certified Critical Prime Dichotomy Lemma
  is vacuous — it never fires, for any core, any index, any prime. Sharp
  (equality attained at `n=2`, `a_1=5`, `p=2`). Reusable as a definitive
  negative screen: forecloses, in general (not just for this problem's
  specific outline), any future FAH mechanism that requires locating a
  genuine "sole rescuer via branch (b)" instance — none exist. Matches the
  spirit of the workspace's other certified vacuity/obstruction results
  (Escape-Cost Vacuity, Same-Type Triangle Vacuity, Generalized
  Class-Blindness Obstruction).
