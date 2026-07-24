# Outline review — round 27, imo-2026-03

Reviewed `/tmp/round-27/proof-outliner.md` against `results/imo-2026-03/current.md` (round-26
log) and the three live approach files. All three outlines are *revise* of already-registered
slugs (no new slugs to seed). Verified independently (re-derivations from scratch, exact
Fraction/float numeric checks) rather than trusting the outline's own algebra — findings below.

## lp-duality-certificate — CHANGES REQUESTED (real gap found in the plan, not just cosmetic)

**Triple-Pin bifurcation Φ=max(p1,T-p1): re-derived from scratch, CONFIRMED.** Composition
(2,0,0,0) pins p1's fragments to (p2,p3,v3), v3=p1-p2-p3. Odd-run-reduction cancels the two
copies each of p2,p3 (even multiplicity), leaving the reduced pair {v3,p4}. Using
A = alternating-sum, sum_odd(full) = (A(reduced)+T)/2 (this identity itself checks out: A =
sum_odd - sum_even, T = sum_odd+sum_even ⟹ sum_odd=(A+T)/2 — a good identity to keep in mind,
the outline doesn't state it explicitly but implicitly uses it). If v3>p4 (⟺ p1>T/2):
A(reduced)=v3-p4=2p1-T, sum_odd=p1. If v3<p4 (⟺ p1<T/2): A(reduced)=p4-v3=T-2p1, sum_odd=T-p1.
Matches the outline exactly, including at the degenerate ladder point (checked n=3 ladder,
v3=p3 numerically-coincident, three-way tie collapses correctly to the same p1 branch via
direct sort-and-sum: Φ=8/15=p1). **Confirmed correct.**

**Bisect1-Sandwich2 Φ=(T+p2-p3-p4)/2: re-derived from scratch, CONFIRMED.** v1=v2=p1/2 cancel
(even pair, zero contribution to A, even rank-shift so parity is preserved for the rest).
Reduced set {w1,w2,p3,p4} in forced order w2>p3>w1>p4 gives A(reduced)=w2-p3+w1-p4=p2-p3-p4;
sum_odd(full)=(A(reduced)+T)/2=(p1+2p2)/2, which equals (T+p2-p3-p4)/2 after substituting
T=p1+p2+p3+p4. **Confirmed correct.**

**The "one genuinely open step" (forced-feasibility lemma: p1>8T/15, p2<4T/15 ⟹ p2>p3+p4) is
correctly flagged as open in the outline's "Open gaps" — but I checked it directly and it is
FALSE, not merely unproved.** Sortedness alone only forces p2>=(T-p1)/3 (since p3,p4<=p2), but
feasibility of Bisect1-Sandwich2 needs the strictly stronger p2>(T-p1)/2. Explicit counterexample:
p=(0.6, 0.15, 0.15, 0.10), T=1 — sorted, p1=0.6>8/15≈0.5333, p2=0.15∈(1/15,4/15), but
p2=0.15 <= p3+p4=0.25, so Bisect1-Sandwich2 is infeasible there. I ran a 200,000-trial random
legal-cut search at this exact point (`/tmp` script, exact result Φ_min≈0.5029 < target 8/15,
best found composition uses **1 cut on p1 and 2 cuts on p4** — cuts=[1,0,0,2]) — so the true
minimizing strategy at this witness is neither Triple-Pin (p1>8T/15 puts it out of scope by the
outline's own step 3) nor Bisect1-Sandwich2 (infeasible), and it is very likely also NOT covered
by any of the 5 old chambers, since round 26's own reviewer already found a nearby point
(3/5,9/40,29/200,3/100) defeats all five. **This means step 5(c)'s fallback ("check whether an
existing chamber already covers it") will almost certainly fail at this exact sub-region, and a
genuinely new chamber family is needed** — the numeric optimal cut pattern (bisect p1, refine
p4 twice) suggests the missing mechanism is a "Bisect1 + p4-refinement" chamber, not yet in the
outline's list.

**Verdict: CHANGES REQUESTED, not RETHINK** — the two new closed-form lemmas are sound and
reusable, and the overall Farkas-covering technique remains the right tool; but step 5(b)'s
"forced-feasibility lemma" must be dropped (it's false, not just unproved) and the builder must
either (a) design a new chamber for the p1>8T/15 corner where p2<=p3+p4 (informed by the numeric
witness above — cuts on p1 and p4, not p1 and p2), or (b) show case (a)'s machinery (p2>=4T/15)
can be stretched to also absorb this corner via a different split. Do not let the builder assume
the fallback chamber check in step 5(c) will succeed without doing it.

## greedy-halving-adversary — APPROVE (with a scope caveat)

**Checked whether the round-24/25 overclaim text has actually been struck this time.** Grepped
the live file: the stale claims ("Combined with Theorem 37 ..., Case (b)'s whole 'v≥a' branch is
now fully, unconditionally closed at n=5" and "...at n=6 as well as n=5") are STILL PRESENT
verbatim (lines ~5867-5872 and ~5897-5903) — but each is now immediately followed by an inline
`[CORRECTED, round 26: ... is FALSE and must not be cited ...]` annotation (lines 5873-5879,
5904-5907) that explicitly flags the claim as false and states the true scope. The file's own
top-of-file round-26 narrative entry (lines 5-41) and the "Net honest status after round 26"
paragraph (lines 5829-5838) are both honestly scoped, with no overclaim. So: **the overclaim has
in fact already been neutralized (not silently deleted, but explicitly annotated as false in
place)** — Step 0 of this round's outline ("strike or correct... before build") is therefore
largely already satisfied; the builder should do a final pass to actually delete/consolidate the
now-redundant stale lines (cosmetic cleanup) rather than treat this as a blocking prerequisite.

**Vertex-domination/local-exchange proposal for the even-tie gap: checked for coherence and
circularity.** The proposed mechanism (perturb one copy of t* in T'' by ±ε, converting the
even-multiplicity tie into an odd-multiplicity tie without decreasing A(B), then invoke the
already-certified Theorem 40 for the odd-tie side) is a genuinely different technique from
Theorem 40's own deletion mechanism (comparison to a *different*, already-solved nearby vertex,
not a re-derivation of the same identity chain under new notation) — this is coherent, not
circular. **However, the outline's own step 5 (cross-front note) states this even-tie gap is
PROVABLY EQUIVALENT, via the Index-Chain Identity, to (star_{n-2}) — the general lower bound one
level down, i.e. the project's central open obstruction.** This means: if the perturbation-
domination argument succeeds, it does not merely close a corner case — it would close the
project's central remaining lower-bound obstruction. This is worth flagging explicitly to the
builder (raise the rigor bar accordingly, and do not be surprised if it does not close cleanly —
both required sub-steps, legality of the perturbed configuration and the sign of the one-sided
derivative, are honestly listed as fully open, not glossed over).

**Verdict: APPROVE** — sound target, sound (non-circular) proposed mechanism, correctly scoped
open gaps; cosmetic cleanup of the redundant-but-already-annotated stale lines recommended, not
required.

## rank-pigeonhole-budget — APPROVE

**Confirmed the outline restricts to the top-cut branch only.** Step 1 explicitly excludes the
top-untouched branch ("do not re-attack that branch this round — it is provably the same
statement [as (star_{m-2})], per math-explorer-general-n.md's proved equivalence"), and step 4
explicitly instructs the builder to prove the closure "citing only sharp-dominant-removal-identity
and Fact 2 ... explicitly NOT citing (star_k) for any k>=3, to keep this genuinely independent of
the central obstruction." This directly satisfies the round's own gate: the m=4 mechanism
generalization is scoped to avoid secretly requiring (star_k) input.

**Sanity-checked the 2-deep dominance chain mechanism.** A(S)=f1-f2+A(R) via two applications of
`sharp-dominant-removal-identity` (peel global max, then new global max) is a correct two-line
consequence of the cited identity provided f1,f2 are each strict maxima at their respective
peeling steps — this was already independently re-verified by the round-26 reviewer at m=4 across
all 5 shapes (5-shape enumeration cross-checked by hand, exact match, no missing/duplicate shape),
so reusing it as the base template for general m is legitimate. The genuinely open content (step
3: does every legal top-cut shape at general m admit *some* 2-deep dominance chain, for shapes
touching >=3 distinct tail indices) is honestly and precisely scoped as fully open — not
smuggled in as "obviously true by analogy to m=4."

**Verdict: APPROVE** — clean scoping, no circularity, genuinely independent front from the
central obstruction as claimed.

## Ranking

Updated via `update_ranking`: rank-pigeonhole-budget and greedy-halving-adversary both clean
outlines this round (draw between them), both beat lp-duality-certificate (which carries a real,
found-false planning step this round, on top of round 26's already-flagged domain-widening bug).
Post-update Elo: rank-pigeonhole-budget 1727.1 > greedy-halving-adversary 1711.5 >
lp-duality-certificate 1619.6 (all `stale` cleared).

## Diversity note

All three approaches remain on genuinely independent fronts (Case-B even-tie vertex vs. general
upper bound n=3 chamber covering vs. MaxCeil/MinFloor top-cut induction) — no shared-gap-plateau
risk this round; continue building all three in parallel.

build set: rank-pigeonhole-budget, greedy-halving-adversary, lp-duality-certificate
