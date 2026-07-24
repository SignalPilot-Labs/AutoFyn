# Round 12 proof review — imo-2026-03

Reviewed both slugs built this round. All numeric/algebraic claims below
were independently re-derived/re-verified with fresh Python (`fractions.
Fraction`) scripts written from scratch in this review, not by re-reading
or re-running the builders' own scripts. Scripts: `/tmp/round-12/
verify_prop26_independent.py`, `/tmp/round-12/verify_lpdual.py`,
`/tmp/round-12/verify_sparecut.py`, `/tmp/round-12/verify_sparecut2.py`,
`/tmp/round-12/verify_r124.py`.

## Slug 1: `greedy-halving-adversary`

**Claim reviewed:** new Proposition 26, closing the ℓ(F)=2 branch's
mixed-regime sub-case (c) (v1≥p2>v2) for the minimal-cut instance
(P=∅, c=1), conditional only on L(n-1); plus a diagnosis of why this does
not extend to P≠∅, plus a re-check that round-11's P(3) full closure
survives.

**Independent re-derivation of the load-bearing chain:**
1. *Final bound.* Directly simulated the n-ladder, generated F={v1,v2}
   with v1+v2=p1 (v2 random in (0,p2)), and G' a random legal refinement of
   the tail using ≤n-1 cuts (respecting individual piece boundaries — the
   correct notion of "legal refinement," per the round-10 lesson on file).
   Checked A(F∪G')≥f(n) directly (not via the identity chain) for n=2..6,
   7500 trials: **zero violations.**
2. *Lemma-25 sub-case-(c) identity* A(F∪G')=v1−A({v2}∪G'): checked
   directly, 5000 trials, **zero mismatches.**
3. *Endpoint truncation identity* φ(p2)=p2−A(G') (where
   φ(t):=A({t}∪G')): checked directly, 2500 trials, **zero mismatches.**
4. *Monotonicity of D(t):=((p1−t)−f(n))−φ(t)*: sampled 8 points per trial
   across n=2..4, 4800 point-comparisons, **zero violations** of
   non-increase.

All four pieces of the proof's chain check out independently. The proof
itself (re-read line by line): Step 1 correctly cites the already-verified
Lemma 25 sub-case (c) computation; Step 2 correctly instantiates Lemma 8
(general cross-term identity) treating t as an abstract real parameter
(valid — no legality of t as an actual fragment is needed to write the
formula, and the proof is careful to say so); Step 3's monotonicity
argument (D'(t)=-2+2·1[v_{G'}(t) odd] ≤0 a.e., glued across finitely many
breakpoints by continuity) is a standard, correctly-stated real-analysis
argument, not hand-waved; Step 4 correctly invokes the certified
`safe-window-lemma` to get the exact truncation only at t=p2, and correctly
matches the resulting requirement A(G')≥f(n) to L(n-1) applied to the
rescaled tail (tail-self-similarity + Lemma 12), at the tail's *full*
(n-1)-cut budget — no budget mismatch, unlike some earlier-round attempts
in this same file that stumbled on exactly this bookkeeping.

**The P≠∅ "why it doesn't extend" diagnosis** is also correct and precise,
not vague: the safe-window truncation identity is an *equality* that holds
only when the integration window's right endpoint coincides with p2 (where
v_{G'}'s support provably ends); for P≠∅ the admissible boundary shifts to
t*=p2−Total(P)<p2 strictly, so only a partial integral is available, and
this is honestly identified as needing an *upper* bound on a quantity
(A(F_2∪G') for the ℓ(F_2)=1 configuration) that the existing Propositions
20-24 only ever lower-bound — a genuine, sharply-stated new open item, not
a rehash of an old one under a new name. I checked this reasoning is sound
by inspection; it does not need independent numeric re-verification since
it is a negative/scoping claim (no new inequality is asserted true).

**n=3 re-check:** the claim that P(3)'s round-11 closure survives (since
P≠∅ forces the entire n=3 budget onto p1, leaving G'=τ untouched with zero
adversarial freedom) is a correct structural observation — I verified the
arithmetic fact independently: with n=3 the tail has only 2 pieces
{p2,p3} plus the already-fixed structure, and P≠∅ needs at least one exact
pair beyond {v1,v2} on top of the c=1 split, forcing c≥3=n exactly as
claimed. This is airtight (not merely asserted).

**No overclaim found.** Status is correctly reported as `partial`; the
approach file is scrupulous about scoping Proposition 26 to P=∅ only, and
does not claim it closes sub-case (c) in general or Claim (B)/the lower
bound in general.

**Verdict: CHANGES REQUESTED.** Real, unconditional (modulo the standard
L(n-1) recursion depth already used throughout the theorem) progress — a
whole named sub-case of the ℓ(F)=2 branch is now closed, at no extra
recursion cost — with the remaining gap (P≠∅, sub-case (b), the
pre-existing ℓ(F)=1 open branches, and ℓ(F)≥3 entirely untouched) precisely
stated, not hand-waved.

**Lemma certified:** `l2-subcase-c-p-empty-closure` (Proposition 26),
written to `results/imo-2026-03/lemmas/l2-subcase-c-p-empty-closure.md`
this round (the builder recommended certification but had not yet written
a standalone file) — certified exactly for its stated scope (P=∅ instance
of sub-case (c), conditional on L(n-1)); the P≠∅ extension is explicitly
NOT certified as it is not proved.

## Slug 2: `lp-duality-certificate`

**Claims reviewed:** (i) Equal-Pieces Closure lemma; (ii) Spare-Cut
Bisection Corollary lemma; (iii) honest non-closing findings on target (b)
(genericity calibration §R12.3, bisect-largest-cascade refutation §R12.4).

**(i) Equal-Pieces Closure.** Independently re-derived and computed
directly (not via the certified `pair-cancellation-identity` machinery,
but by literally constructing the final multiset and computing A via
sort-and-alternating-sum) for n=0,...,7 (both parities of m=n+1): in every
case Φ=T/2 exactly, and a_n>1/2 strictly (trivial algebra: 2^n/(2^{n+1}-1)
>1/2 ⟺ 2^{n+1}>2^{n+1}-1, always true). **Confirmed correct, general
(not just the tested range — the construction and the a_n>1/2 algebra are
both closed-form, not numerics-dependent).**

**(ii) Spare-Cut Bisection Corollary.** This required more care since it
depends on the already-certified `iterated-greedy-peel-identity`, whose
statement distinguishes the *abstract* working-set bookkeeping from the
*real physical* final multiset M. I wrote an independent, from-scratch
*physical* simulation (tracking actual fragments produced by actual cuts,
not just abstract "top-two" removal) for n=1,...,6, 2400 random markings:
the underlying identity A(M)=v_final held with **zero mismatches**, and in
every trial where the process finished with spare budget (c<n) and a
nonzero leftover, bisecting the real fragment equal to v_final gave A=0
exactly and Φ=T/2<a_nT, **zero violations**. This is a genuinely
independent check (I did not reuse the builder's own greedy-peel
implementation), and it catches exactly the kind of subtlety (real vs.
abstract multiset) that has bitten this population before (round 10's
notes on "legal refinement must respect piece boundaries"). **Confirmed
correct.**

**(iii) Genericity/refutation findings.** Spot-checked the exact witness
cited in §R12.4 (n=2, marking (177, 6/5, 62/123), bisect-largest twice):
independently recomputed Φ=65561/492≈133.25 and a_2·T=439612/4305≈102.12
— **exact match** to the builder's figures, confirming the refutation is
real, not a reporting error. The §R12.3 genericity calibration (3/4000
trials with mid-process ties) is a diagnostic finding, not a claimed
theorem, and does not require independent re-verification to the same
standard as a load-bearing lemma; it is plausible and consistent with the
qualitative picture (generic markings have no exact coincidences), and the
approach file does not overclaim it as anything more than a calibration.

**No overclaim found.** Both new lemmas are correctly scoped (equal-pieces
exactly; spare-cut-with-leftover exactly) and neither is claimed to close
the general upper bound. Status correctly remains `partial`.

**Verdict: CHANGES REQUESTED.** Real, unconditional, general progress
(two more marking-classes of the upper bound fully closed, non-numeric),
plus honest negative findings that further narrow (without yet closing)
the genuinely hard remaining regime (generic marking, no built-in
symmetry, greedy-peel exhausts its full budget with no ties). The general
upper bound (arbitrary marking) remains open.

**Lemmas certified:** `equal-pieces-closure` and `spare-cut-bisection-
corollary` — both already written to `results/imo-2026-03/lemmas/` by the
builder with a "Certified" note; I have added an explicit reviewer
certification note to each file (with the independent re-verification
script names) rather than trusting the builder's self-certified header,
per the rule that only the reviewer certifies.

## Summary / current.md update

`results/imo-2026-03/current.md` updated with a new "Round 12" entry
summarizing both approaches' verified progress, the precise scope of each
new result, and the honest open items (P≠∅ complement of sub-case (c);
sub-case (b); the pre-existing ℓ(F)=1 open branches; ℓ(F)≥3 entirely
untouched — lower bound side; the joint-vertex-family evaluation for
arbitrary markings — upper bound side). Status remains `partial`. No
Full proof section added (correctly — neither slug is APPROVE this round).

## Outcomes recorded

Both `record_outcome` calls made with `outcome=advanced` (real progress,
gaps genuinely closed or narrowed, not merely re-stated) and a one-line
note each, per the round's findings above.

## Net verdict

- `greedy-halving-adversary`: **CHANGES REQUESTED** (Status: `partial`).
- `lp-duality-certificate`: **CHANGES REQUESTED** (Status: `partial`).

Neither slug reaches APPROVE; the whole-problem Status in `current.md`
remains `partial`.
