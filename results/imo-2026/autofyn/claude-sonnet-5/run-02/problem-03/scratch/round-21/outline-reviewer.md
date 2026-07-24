# Outline review — round 21, imo-2026-03

Reviewed `/tmp/round-21/proof-outliner.md` against `results/imo-2026-03/current.md`,
`approaches/{greedy-halving-adversary,rank-pigeonhole-budget,lp-duality-certificate}.md`,
and `.ranking.json`. All three are revisions of already-registered, mature approaches
(no new slugs this round). I re-derived the load-bearing algebra independently with
sympy/exact-Fraction scripts rather than trusting the outline's prose.

## greedy-halving-adversary — APPROVE

**Whole attempt?** Yes — still the same top-level lower-bound approach (potential-
function induction + explicit adversary strategy), now targeting the precisely-named
ε-bridge crux round 20 uncovered. Not a fragment split off into a new slug.

**Step 2 mechanism ("closes for free via substitution") — VERIFIED, not just plausible.**
I substituted the floor lemma's lower bound Ξ ≥ v−s′−2v·ε′(v) into
Δ(n,v) = −p₃−Ξ, then symbolically compared the resulting upper bound on Δ(n,v)
against the target v−f(n)−2v·ε(v) with ε(v)=1−ε′(v) and f(n)=p₃−s′ substituted in.
`sympy.simplify` gives the difference is identically **0** — the two sides are the
same expression term-for-term, exactly as claimed, for both values of ε′(v)
simultaneously (no case split). I also independently re-verified the two feeder
identities used (f(n)=p₃−s′, p₂=2p₃, f(n)+s=p₂) numerically against the exact ladder
for n=3..7 with exact `Fraction`s — all hold exactly. This step is sound.

**Step 3 (boundary sub-range s′<v<p₃) — VERIFIED.** Reduced target A(T′)≥v−s′
algebraically checks out (v+f(n)−p₃ ≡ v−s′ once f(n)=p₃−s′ is substituted,
confirmed by sympy), and citing Theorem 35b's own A(T′)≥f(n)·2^{n−3}≥f(n) as a
strictly stronger bound is valid since v−s′<f(n) in this sub-range (v<p₃=s′+f(n)).
Correctly scoped as unconditional (Fact 1 alone, no IH needed) — matches the file.

**Step 4 and step 6 — correctly left open, not overclaimed.** The outline is careful
to say Theorem 35b's own ε-bookkeeping is "likely free... write out explicitly, do
not assume." I checked the trivial fact it relies on (v≥p₃ ⟹ R′_{>v}=T′_{>v} exactly,
so ε(v)=ε′(v) with no shift) — true, but the outline correctly does not claim the
downstream substitution is automatically free; it's flagged as a to-do. Step 6
(Case (b), the p₃-is-cut branch) is explicitly marked "NOT yet verified even in
outline form" — accurate; the file's own Case (b) section (round 19/20) is honestly
still open beyond n=3,4, and nothing in the outline overclaims past that.

**Verdict: APPROVE.** No fixable gaps beyond what the outline itself already flags.

## rank-pigeonhole-budget — APPROVE

**Whole attempt?** Yes, same slug/history (Claim (A) already solved; this round's
slice is the sibling §7.5/§7.6 cross-check of the shared ε-bridge). Importing the
Band-Parity Fact rather than re-deriving is appropriate (shared lemma, not a fork).

**Tightened bound mechanism — VERIFIED exactly.** The true (ε-corrected) target in
§7.5's middle band (v₂∈[p₄,p₃), where ε(v₂)=1 since |τ_{>v₂}|=1 is odd) reduces to
v₁+v₂ ≤ s+3p₄ = 6p₄ (I re-derived this reduction by hand from Δ(3,v₂)=−3p₄, matching
the file's own §7.5 computation, and the outline's stated target). Plugging in exact
ladder values at n=3 (p₄=1/15, p₃=2/15, p₂=4/15, s=1/5): p₂=4p₄ and p₃=2p₄ exactly,
so v₁<p₂=4p₄ and v₂<p₃=2p₄ (the case hypothesis, tighter than the old proof's
v₂>0) give v₁+v₂<6p₄ strictly — confirmed by direct Fraction arithmetic, not just
symbolically. This closes the whole ε-corrected middle band at n=3, cleanly.

**Step 3/4 — correctly scoped.** The outline explicitly separates "closed the n=3
epsilon-bridge" from "closed §7.6's general-n gap" (the cross-piece tie-vertex
enumeration), and flags this exact distinction as something round 20's reviewer
already caught the sibling almost conflating — good, self-aware scoping, matches
the file's own honest §7.6 write-up (untouched, pre-existing open item).

**Verdict: APPROVE.**

## lp-duality-certificate — CHANGES REQUESTED

**Whole attempt?** Yes — same slug, now pivoting within its own general-upper-bound
target to a primal chamber-vertex framing for case (b2), the sole remaining open
region after 6-7 prior mechanism families (peel/bisect/recurse, weighted-combination,
boundary-continuity, Danskin/concavity, surrogate/majorization, constraint-side LP
dual) were confirmed dead across rounds 8-19. The exact tally in the outline's prose
("7 confirmed-dead") is slightly loosely counted across the file's own inconsistent
round-by-round numbering (round 17 said "fifth", round 18 "fourth", round 19
"sixth") — cosmetic, not load-bearing; flag for the builder to state the count
precisely (list the mechanisms by name) rather than repeat an unverified ordinal.

**Genuinely distinct from the two closest dead mechanisms — confirmed.**
- vs. `minimax-lp-response-polytope` (dead, constraint-side LP dual): that mechanism
  dualizes Xiang Yu's response-polytope *constraints*; this approach fixes Liu Bang's
  own marking p as the *primal* variable being maximized over — a different object
  entirely (outer maximization vs. inner dual), not a resurrection.
- vs. the dead Danskin/global-concavity mechanism (round 18): the outline correctly
  locates the round-18 V-shaped interior local min at p₃=p₁−p₂, which is exactly a
  response-type switch point (chamber wall) per `per-piece-vertex-decomposition-
  theorem`'s tie/zero pattern — consistent with the file's own round-18 record. The
  new claim is explicitly *local* (within one fixed chamber), which is a strictly
  weaker and different requirement than the refuted *global* concavity — legitimate.

**Within-chamber affinity (Key Lemma, step 2) — mechanism is mathematically sound in
principle, but the citation chain has a real gap the outline underplays.**
`per-piece-vertex-decomposition-theorem` (certified) only establishes that each
piece's optimal fragmentation is *itself* a vertex relative to the other pieces'
current values — it does **not** state or prove that the resulting coordinates are
affine functions of p; the phrase "Cramer's rule" / "affine function of p" appears
nowhere in the cited lemma or anywhere pre-existing in the approach file (checked by
grep — zero hits before this round). The underlying reasoning is legitimate: within
a fixed combinatorial tie/zero type, the joint linear system (mass-conservation rows
with RHS = p_i, tie/pin rows with p-independent, 0 or equal-value RHS) has a
coefficient matrix depending only on the combinatorial type, so if the system is
uniquely solvable (a genuine vertex), the solution is linear in p — I sanity-checked
this principle on a toy example (f₁=f₂=p/2, f₃=0) and it is correct in kind. But
**uniqueness/well-posedness of the joint mutual system across all m pieces
simultaneously (not just one piece at a time) is not yet argued anywhere** — this is
exactly what the outline's own "Open gaps (a)" flags as needing to be written out,
so the outline is honest about it, but Step 2's Key-Lemma writeup ("direct
consequence of step 1's coordinate formula") overstates how much step 1 already
gives; the builder should not treat affinity as free once step 1 is cited — it is a
new derivation, not a corollary, and should be stated as such (the outline's own
"Open gaps" section already says this correctly; the "Key lemmas" section's
one-line mechanism blurb is the part that reads more free than it is).

**Chamber-count risk — correctly flagged, not resolved.** The outline itself gates
further investment on a computational chamber-count check at n=3,4 before scaling to
general n (step 5b) — appropriate caution, keep this as a hard gate before the
builder invests in the general-n write-up.

**Verdict: CHANGES REQUESTED.** Proceed with the build (framing is sound and
genuinely new), but the builder must (1) actually carry out the well-posedness
argument for the joint tie/zero linear system (not just cite step 1 and assert
affinity), and (2) run the n=2,3 gates (steps 5a-5c) before writing any general-n
claim, exactly as the outline's own step 5 already requires — do not let step 2's
Key-Lemma phrasing skip past this in the write-up.

## Cross-cutting note on field diversity

Fronts 1 and 2 share the identical Band-Parity Fact and identical substitution
mechanism, applied to two different sibling proof files' own separate case splits
(Theorem 35a/35b's Δ(n,v) vs. §7.5's Δ(n,v₂)-style target). This is not a "one proof
split across two slugs" violation — each slug is an independent whole attempt with
its own multi-round history and other closed sub-results (Claim (A) fully solved
under rank-pigeonhole-budget; the c₁≤1/ℓ(F)≤2 lower-bound ladder under
greedy-halving-adversary) — but it does mean both fronts share one crux: if the
Band-Parity Fact or the f(n)=p₃−s′ identity turned out flawed, both would fail
together. I independently re-derived both facts from scratch (not by trusting the
Fact's name) and both check out exactly, so this is currently low risk, but future
rounds should keep tracking this as a shared dependency, not treat the two fronts as
fully independent corroboration of each other.

Front 3 (lp-duality-certificate) is genuinely far from fronts 1/2 in both target
(general upper bound vs. restricted lower bound) and technique (primal
chamber-vertex extremal argument vs. direct alternating-sum substitution) — good
diversity across the build set.

build set: greedy-halving-adversary, rank-pigeonhole-budget, lp-duality-certificate
