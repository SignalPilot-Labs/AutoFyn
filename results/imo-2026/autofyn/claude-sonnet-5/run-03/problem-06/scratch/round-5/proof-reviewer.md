# Proof review — imo-2026-06, round 5

Reviewed all 5 built approaches. All independently verified by hand/computation
(Python + sympy for exact-integer simulation, direct re-derivation of every
load-bearing algebraic/combinatorial step). Verdict summary:

| Slug | Status | Verdict | Ranker outcome |
|---|---|---|---|
| active-set-stabilization | partial | CHANGES REQUESTED | advanced |
| renormalization-induction-on-seed | partial | CHANGES REQUESTED | advanced |
| scalar-difference-pigeonhole | partial | CHANGES REQUESTED | advanced |
| frozen-invariant-monovariant | partial | CHANGES REQUESTED | advanced |
| state-compactness-pigeonhole | partial | CHANGES REQUESTED | advanced |

No RETHINK, no APPROVE. `current.md` remains Status = `partial`. The problem
is NOT solved. All 5 builders correctly self-assessed Status `partial` — no
overclaiming detected anywhere this round.

`results/imo-2026-06/current.md` updated with a "Round 5 additions" section
summarizing all 5 approaches' new content. 12 new lemmas certified into
`results/imo-2026-06/lemmas/` (list below). All 5 outcomes recorded via
`mcp__approach-ranker__record_outcome`.

---

## 1. active-set-stabilization — the ρ(n)≥2 counterexample (dispatch focus)

**Claim reviewed:** refutes the round-5-assigned "Redundancy Growth Lemma"
(hoped: ρ_Q(n):=|R(a_n)∩Q_min|≥2 eventually blocks new elements entering
Nec) via a hand-verified counterexample at a_1=35.

**Independent verification.** I re-ran the exact greedy sequence from
scratch in Python (`sympy.gcd`/`factorint`), *not* trusting the builder's
arithmetic:

```
a_1..a_4 = 35, 40, 42, 45
R(a_1)={5,7}, R(a_2)={2,5}, R(a_3)={2,3,7}, R(a_4)={3,5}
```

This matches the builder's hand computation exactly. The four claimed
singleton intersections all check out:
R(a_1)∩R(a_3)={7}, R(a_1)∩R(a_2)={5}, R(a_2)∩R(a_3)={2}, R(a_3)∩R(a_4)={3}
— so Q_0={2,3,5,7}⊆Nec⊆Q_min is correctly established.
ρ_{Q_0}(1)=|{5,7}∩Q_0|=2, ρ_{Q_0}(2)=|{2,5}∩Q_0|=2 — both confirmed by
direct set intersection. Yet R(a_1)∩R(a_2)={5}, size 1 — confirmed. So the
implication "ρ(i)≥2 and ρ(j)≥2 ⟹ |R(a_i)∩R(a_j)|≥2" is **genuinely false**,
already at the first pair. The structural diagnosis ("marginal statistics
never control joint intersections") is correct elementary set theory.

I also independently re-simulated the secondary a_1=21 claim (every term
divisible by 3, ρ(n)<2 recurring infinitely often despite self-sufficiency
via a "universal prime" mechanism): confirmed — the first 25 terms of the
a_1=21 sequence are all multiples of 3.

**Verdict:** the refutation is correct and decisive, not a strawman. This
kills a 4th/5th-generation proposed mechanism cleanly (joining the growing
"dead mechanisms" list). No progress toward the central gap itself. Status
partial (correctly self-assessed). **CHANGES REQUESTED.**

Certified: `lemmas/redundancy-marginal-insufficiency.md` (negative).

---

## 2. renormalization-induction-on-seed — Minimum Gap Lemma + Even-Seed
Universal Lock Theorem (dispatch focus — strong claim, checked hard)

**Minimum Gap Lemma:** a_{n+1}≥a_n+2 for every n≥1. Proof: gcd(a_n+1,a_n)=1
(consecutive integers), so a_n+1 fails the i=n constraint, hence is never a
valid candidate; combined with strict monotonicity, a_{n+1}≥a_n+2. This is
a completely correct, trivial-but-real three-line argument — I re-derived it
independently and it holds with no hidden case.

**Even-Seed Universal Lock Theorem:** if a_1 is even, a_n=a_1+2(n-1) for
every n≥1, i.e. **T=1, L=2 exactly, for the entire even-a_1 sub-family, no
transient.** This is claimed as a full, rigorous, unconditional solve of an
entire infinite sub-case of the IMO problem.

**My independent check of the induction.** Base case: a_1+2 is legal
(gcd(a_1+2,a_1)=gcd(2,a_1)=2>1 since a_1 even; only constraint at n=1 is
i=1), and by Minimum Gap a_2≥a_1+2, and the only smaller integer a_1+1 is
excluded — so a_2=a_1+2 exactly, and it's even. Inductive step: given
a_1..a_n all even, a_n+2 is even, so gcd(a_n+2,a_i)≥2 for every i≤n
(both even) — legal; the only smaller candidate a_n+1 is excluded by
Minimum Gap (needs no inductive hypothesis, holds unconditionally at index
n); hence a_{n+1}=a_n+2 exactly, even. This closes the induction rigorously,
no gaps, no skipped cases (the case split is total: only two candidates,
a_n+1 and a_n+2, need to be checked, since anything larger is automatically
not minimal once a_n+2 is shown legal).

**My independent numerical re-verification** (not trusting the builder's
own check): ran the exact greedy sequence for a_1 ∈
{2,4,6,10,12,30,210,194,10^8}, 20 terms each — every case matches
a_n=a_1+2(n-1) exactly, zero deviations, including the very large seed
10^8 (rules out any "small-seed coincidence" concern).

**Overclaim check.** The builder correctly states Status remains `partial`
for the approach as a whole (only the even sub-family is closed; general
odd-min-prime case remains open) — no overclaim to `solved` anywhere. The
honest diagnosis of why the technique doesn't extend to odd p (p−1
in-between candidates vs. only 1 excluded by the free Minimum Gap Lemma) is
correct and precisely locates the remaining difficulty.

**Verdict:** this is genuine, fully rigorous, independently-verified
progress — the first time any approach in the 5-round population has fully
closed an entire infinite sub-case of the general problem end-to-end (not
just a lemma toward it). Still `partial` overall since only one sub-family
is settled. **CHANGES REQUESTED** (re-dispatch to push the induction further,
e.g. p=3 next).

Certified: `lemmas/minimum-gap-lemma.md`,
`lemmas/even-seed-universal-lock-theorem.md`.

---

## 3. scalar-difference-pigeonhole — Positive-Density Upgrade + Sharpened
Bounded-Gap Lemma (dispatch focus)

**Positive-Density Upgrade (Lemma 3).** Standard finite-alphabet
limsup/subadditivity argument: assumes-for-contradiction that every value
v∈[T,TR] has limsup c_v(N)/N < 1/m, derives a strict-sum contradiction with
Σc_v(N)=N. I re-derived this from scratch independently — it is a correct,
standard pigeonhole-density argument (the ε-choice as a minimum of finitely
many positive numbers, and the N_0 as a finite max, are both handled
correctly; no off-by-one or quantifier-order error). The remark that this
same L(T) also witnesses plain infiniteness (via monotonicity of c_v(N) in
N) is also correct.

Caveat honestly flagged: only *upper* density, not lower density or
syndeticity — correctly stated as insufficient, no silent upgrade attempted.

**Sharpened Bounded-Gap Lemma (Lemma 4).** Re-derivation of the internal
"Fact" already inside `bounded-gap-via-rad-a1.md`'s own proof, splitting
into the r_n=0 and r_n≠0 cases. I checked this against the parent lemma's
proof (`bounded-gap-via-rad-a1.md` uses M=R(⌊a_n/R⌋+1) as a legal
candidate) — correct, a genuine and correctly-derived tightening.

**§4's honest stall report** (Fekete's lemma inapplicable — no
subadditivity relation known; Lemma 3+Lemma 4 don't compose because
membership in Y_T isn't linked to r_n) — both claims are correctly
reasoned: the greedy rule's legality genuinely depends on the *entire*
prefix's full factorization, not a two-term recursion, so there is no
evident subadditive inequality; and no link between r_n and Y_T membership
is established or claimed.

**Verdict:** both new lemmas are correct, unconditional, and reusable; the
approach honestly reports it cannot yet close the syndeticity target.
`partial`, correctly self-assessed. **CHANGES REQUESTED.**

Certified: `lemmas/positive-density-upgrade.md`,
`lemmas/sharpened-bounded-gap-lemma.md`.

---

## 4. frozen-invariant-monovariant — well-definedness + negative transplant
diagnosis (dispatch focus)

**Prefix-Support Stabilization Lemma (§2.1).** Standard finite-monotone-
stabilization argument (S_n(p,M) non-decreasing subset of the fixed finite
set Z/MZ). Correct, elementary, no gap.

**Well-definedness of w_n(M) (Lemma 2, §2.2).** I re-derived the residue-
class-partition argument independently: N:=lcm(Q); divisibility by any
p∈Q depends only on m mod N; if π_{n+1}(M)≠Q, the class m≡0 (mod N) fails
to match (since R(m)∩Q=Q≠π); if π_{n+1}(M)=Q, the class m≡1 (mod N) fails
(R(m)∩Q=∅≠Q, using Q≠∅ since a_1>1). Either way a full residue class
inside (a_n,a_n+N] fails to match. This is correct and complete — verified
both sub-cases myself, no gap.

**Negative diagnosis (§3.2–3.3, "aimo-0678-mechanism inapplicability").**
This is the harder claim to verify: it argues (a) no recurrence-intrinsic
frozen quantity exists (correct and easy: legality depends on the entire
variable-length prefix, not a bounded two-term update — a genuine
structural contrast with aimo-0678's s_n=a_n+b_n identity) and (b) no
bounded-window break-point classifier exists, by "the same argument"
applied to `windowed-epsilon-automaton-failure.md`.

I scrutinized (b) carefully since it is stated somewhat tersely ("the same
argument applies verbatim ... by the identical argument"), which risks
being exactly the kind of hand-waving CLAUDE.md forbids. On inspection the
underlying mathematical content is sound and does generalize: under the
hypothesis that (d_n,ℓ_n) is eventually constant =(d*,ℓ*), a_n mod any
fixed modulus L cycles with period L/gcd(d*,L) — a standard fact about
arithmetic progressions mod L, which the certified windowed-epsilon lemma
already established for L=R and is straightforwardly re-derivable for
L=lcm(R,M) by the identical computation (a_n = a_{n0}+d*(n-n0), so a_n mod
L is a genuine arithmetic progression mod L). This is not a citation of a
different problem's crux move (forbidden) — it is reusing the population's
own already-certified in-house lemma and correctly re-deriving the
generalization inline, so it does not violate the "no crux move
references" rule. I judge this correct but slightly under-spelled-out; not
a fatal gap, but flagged in the certified lemma file as "stated somewhat
tersely" so a future round tightens it if reused as a load-bearing step
elsewhere.

**Verdict:** genuine free lemmas (well-definedness, Prefix-Support
Stabilization) plus a real, mostly-rigorous negative diagnostic result that
correctly narrows what any successor construction must look like. `partial`,
correctly self-assessed (does not claim to close the central gap).
**CHANGES REQUESTED.**

Certified: `lemmas/universally-dividing-prime-set-stabilizes.md`,
`lemmas/prefix-support-stabilization.md`,
`lemmas/pattern-violation-monovariant-well-definedness.md`,
`lemmas/aimo-0678-mechanism-inapplicability.md` (negative, minor rigor
caveat noted above).

---

## 5. state-compactness-pigeonhole — Multiple-of-R Realization Lemma +
Same-Class-Free Lemma (dispatch focus)

**Multiple-of-R Realization Lemma (§12.1).** Claim: every x>a_1 with
rad(a_1)|x is *itself an accepted term*, not merely a legal candidate
(strictly stronger than the existing `bounded-gap-via-rad-a1.md`). Proof
uses the certified `prime-factors-a1-cover-forever.md` (every a_i shares a
prime with R(a_1)) plus greedy minimality: picks k maximal with a_k<x,
shows x is legal at step k (every a_i, i≤k, shares a prime p∈R(a_1) with
x, since p|R|x), so a_{k+1}≤x, and a_{k+1}≥x by maximality of k, giving
a_{k+1}=x exactly. I re-derived this independently — correct, no gap.

**My independent numerical re-verification** (Python, exact-integer greedy
simulation, 800 terms each): for a_1 ∈ {15,21,35,45,63,105,375}, checked
*every* multiple of rad(a_1) beyond a_1 against the generated term set —
**zero missing multiples** in all 7 cases, consistent with the lemma.

**Same-Class-Free Lemma / Class-Partition Reduction (§12.2–12.3).**
π(n):=min(R(a_n)∩R(a_1)); same-π-class pairs automatically share a prime
of R(a_1)⊆Q_min. I re-checked the proof (one-line: p:=π(i)=π(j) divides
both a_i,a_j and lies in P⊆Q) — correct. The corollary (Nec-witnessing
pairs outside P must be cross-class) follows by direct contrapositive,
also checked and correct. §12.3 honestly reports (via computation, clearly
labeled as evidence not proof) that this reduction alone is insufficient —
the residual cross-class "P-problematic" pair set is not shown finite; no
overclaim.

**Bounded index-gap refutation (§12.4).** Claim: "consecutive elements of
I_p differ in index by ≤p" is false; counterexample a_1=385, p=5, index
gap 6>5. I independently re-simulated a_1=385 from scratch in Python:
a_1..a_8 = 385,390,392,396,399,406,418,420 — **exact match** with the
builder's hand computation. Checked I_5 membership directly:
5|385,390,420 only among a_1..a_8; consecutive elements at indices 2 and 8,
gap 6>5 — confirmed exactly as claimed.

**Verdict:** all three round-5 results check out independently — one
genuinely new unconditional structural fact (Multiple-of-R Realization), one
correct-but-honestly-insufficient reduction, and one correctly-refuted
proposed mechanism. `partial`, correctly self-assessed, no overclaim.
**CHANGES REQUESTED.**

Certified: `lemmas/multiple-of-r-realization.md`,
`lemmas/same-class-free-class-partition-reduction.md`,
`lemmas/bounded-index-gap-refutation.md` (negative).

---

## Overall assessment / notes for next round

- The problem remains open (`current.md` Status = `partial`); no false
  `solved` claim anywhere this round — all 5 builders' self-reported
  Status matched what I independently found.
- **Headline result of the round:** `renormalization-induction-on-seed`'s
  Even-Seed Universal Lock Theorem is qualitatively different from every
  other lemma certified so far in this run — it is not a structural fact
  *about* the central gap, it is a **complete, unconditional solve of an
  entire infinite sub-case of the actual IMO problem** (T=1, L=2 for every
  even a_1). This is real, verifiable evidence the induction-on-ω(a_1)
  architecture can fully close cases, not just approach them asymptotically.
  Next natural target: the odd-prime case p=min R(a_1)=3 (the smallest case
  the Minimum-Gap-only argument does not cover), since §7.4 precisely
  diagnoses what's needed (control of p-2≥1 "in-between" candidates).
- A sixth and seventh mechanism were cleanly killed this round
  (Redundancy Growth Lemma; bounded index-gap ≤p density mechanism),
  joining the population's growing "confirmed-dead mechanisms" list — all
  independently re-verified, none were strawmen.
- Two genuinely new architectures (`scalar-difference-pigeonhole`,
  `frozen-invariant-monovariant`) both produced real free lemmas on their
  first full build and both honestly diagnosed exactly where they stall,
  rather than overclaiming — good population health, no red flags.
- Minor rigor note (not gate-affecting): `frozen-invariant-monovariant`'s
  §3.3 negative-diagnosis step ("the same argument applies verbatim")
  is correct but terser than ideal — flagged in the certified lemma file;
  a future round citing `aimo-0678-mechanism-inapplicability.md` as
  load-bearing for a stronger claim should re-spell out the cycling
  argument in full rather than lean on the "verbatim" phrasing.
