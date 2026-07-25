## imo-2026-06 — outline review, round 2

### Critical process finding (fix before reading further)

The outliner's report `/tmp/round-2/proof-outliner.md` (mtime 23:24:57) is timestamped
**after** every file in `results/imo-2026-06/approaches/` (all last modified 22:54–23:09,
i.e. round-1 content). Verified by grep: none of the round-1 `.md` files contain any of
the round-2 vocabulary ("cofinite," "S is false," "self-sufficiency stopping criterion"
reframe, etc.) that the outliner's report claims to have written into them. **The
outliner wrote its revision plan only to its own report file, never persisted it to the
approach files it was dispatched to update.** Also, `bounded-window-tournament.md` (the
"new" approach in the outliner's report) does not exist anywhere on disk.

Since builders read `approaches/<slug>.md`, not the outliner's chat report, this would
have silently sent every builder back to stale round-1 text — including the refuted
"S finite" target — wasting the entire round. **I have fixed this myself**: I
transcribed each approach's round-2 revision (from the outliner's report) into a new
"Round 2 revision" section at the top of the corresponding `.md` file, and, in the
process of transcribing, actually checked the outliner's proposed mechanisms for
soundness (per this round's dispatch instruction) rather than passing them through
verbatim. Two of the four proposed mechanisms turned out to be unsound as stated (see
below) — good thing this was caught before build.

`bounded-window-tournament` was NOT materialized (no file → nothing to register or
build); flagged for next round.

---

### Reframe (binding on the whole population) — VERIFIED SOUND

Claim: S := {p : p | a_n for infinitely many n} is provably **infinite** (cofinite in
the primes), not finite. Proof sketch (checked): if a_{n+T}=a_n+L holds for n≥n0 (the
target conclusion), fix residue r mod T; the sub-progression a_r, a_r+L, a_r+2L,...
has common difference L, and for any prime p∤L, L is invertible mod p so this AP hits
0 mod p infinitely often ⟹ p∈S. Hence every prime not dividing the (finite) L is in S,
i.e. S is cofinite. This is correct, non-circular (it uses the conclusion to derive a
necessary structural fact, a legitimate proof-by-necessary-condition move, not a
petitio), and matches the numerics cited (a_1=15: every prime ≤409 recurs). **Approved
as the new binding target**: the finite object to build is L (equiv. Q=rad(L)⊆S), not S
itself. All four approaches below were correctly retargeted at L.

---

### jacobsthal-covering-bound — CHANGES REQUESTED, advance

Sound skeleton: phase induction Q_0=rad(a_1), recruit new prime only when the greedy
step needs one outside Q_j, terminate when self-sufficient. Step 1 (g(Q)=min(Q) covering
gap) and step 4 (import residue-pigeonhole finish once Q is known finite) are correct
and reusable.

**Issue.** Step 3, the termination monovariant — the ONE genuinely hard new claim this
round — is not a lemma, it is prose that talks about the goal ("no candidate can ever
again beat the guaranteed one... becomes combinatorially harder each phase") without a
checkable inequality. The outline itself flags this honestly as open, which is good, but
it must not be mistaken for "almost closed." Told the builder explicitly: produce a
concrete inequality (in Q_j, g(Q_j), density) or a genuinely different phase-count bound,
and do not reuse growth-rate-contradiction's now-refuted window-position mechanism (see
below) as a shortcut.

### active-set-stabilization — CHANGES REQUESTED, revise

The already-correct residue-mod-L pigeonhole finish (given L finite) stands: this
approach's job is now division-of-labor (import L from jacobsthal, supply T + the
prefix-extension fix).

**Issue found (real unsoundness, not a nitpick).** The outliner's proposed fix for the
secondary "extend eventual periodicity to all n≥1" gap — "σ has finitely many values, σ(1)
is one of them, so by pigeonhole some later index repeats σ(1)" — is a **pigeonhole
fallacy**. Finite codomain + infinite domain guarantees SOME state recurs infinitely
often; it does NOT guarantee the specific starting state σ(1) is among the recurring
ones. This is exactly the standard failure of eventually-(not purely-)periodic orbits of
a function on a finite set: σ(1) can be a genuine transient, visited once, never on the
eventual cycle (concretely: the state's residue-multiset component only grows until
saturation, so the pre-saturation dynamics differ structurally from the post-saturation
map, and there's no a priori reason the latter is a bijection). I rewrote the file's
Round 2 section to reject this specific fix and give the builder three legitimate
options: (a) prove the eventual map is a genuine permutation (new claim, must be proved),
(b) explicitly absorb the finite pre-saturation transient into an enlarged T/L by direct
finite computation, or (c) honestly report periodicity only for n≥n1 (still `partial`,
not a failure). Builder must not resubmit the fallacious argument as a closed gap.

### state-compactness-pigeonhole — CHANGES REQUESTED, revise (complement-set framing)

Genuinely different bookkeeping device from active-set-stabilization (periodicity of the
*set* B=Z_{>1}∖{a_n} rather than of a difference sequence) — good diversity, not a
same-framing duplicate. Correctly self-flagged by the outliner: step 3's "exactly"
claim needs the identical self-sufficiency mechanism jacobsthal is missing, approached
from the complement side — i.e. this is a second, independent route to the SAME open
lemma, useful as a cross-check, not an independent closure. I preserved this honest
framing in the file and added the same warning against the active-set-stabilization
pigeonhole fallacy (a builder here would be equally tempted to reuse it for the same
prefix-extension gap).

### growth-rate-contradiction — RETHINK (do not build this line again)

**The proposed new mechanism is mathematically FALSE, not merely under-tightened.**
Claim tested: "p_0 < g(Q_j) is necessary for a fresh prime p_0 to be recruited" (since
a recruiting candidate m must lie within g(Q_j) of a_n and be divisible by p_0).
Counterexample (verified numerically): choose a_n ≡ -1 (mod p_0) for ANY prime p_0 — the
very *first* multiple of p_0 after a_n is a_n+1, distance 1, independent of how large
p_0 is (e.g. p_0=97, a_n=96, distance 1). So a huge prime's first multiple can land
arbitrarily close to a_n purely by residue alignment; "p_0 divides something near a_n"
carries no upper bound on p_0. The outline's own caveat ("only works for the first
multiple") does not rescue it — the counterexample already uses the first multiple. This
kills the whole "window-position" mechanism, not just its edge cases; no amount of
tightening produces a valid necessary condition of this shape. Combined with round 1's
already-dead counting mechanism, this approach has now failed twice with no independent
idea left for the central gap. Recommend: do not dispatch a builder on this skeleton
again; either retire it or have next round's outliner propose a genuinely different
mechanism (not a variant of "bound the recruit via local window position"). The
certified bounded-gap lemma from this approach remains valid and in use by the others.

### bounded-window-tournament — not reviewable (no file), not registered, not built

The idea (finite bit-vector state ρ(n)∈{0,1}^R over the literal candidate window) is a
plausible, genuinely different bookkeeping device worth trying, but per CLAUDE.md's
one-slug-one-file contract there is nothing on disk to review or hand to a builder.
Not registered this round (registering a slug with no approach file would pollute the
ranked population with a phantom entry). Recommend: next round's outliner must actually
write `results/imo-2026-06/approaches/bounded-window-tournament.md` before it can be
registered or built.

---

### Ranking

Ranked head-to-head via `update_ranking` (ordering now, best-first):
state-compactness-pigeonhole (1538.7) ≈ active-set-stabilization (1534.6) >
jacobsthal-covering-bound (1484.7) > growth-rate-contradiction (1442.0, now doubly
dead-ended on its central mechanism).

Rationale: state-compactness-pigeonhole and active-set-stabilization drew against each
other (both are essentially complete modulo importing jacobsthal's L plus their own
flagged, non-trivial finishing gap) and both beat jacobsthal and growth-rate-contradiction
(jacobsthal supplies the genuinely open bottleneck lemma everyone depends on, so it's
necessary but currently the least-developed; growth-rate-contradiction's new idea was
refuted this round, on top of round 1's refuted idea).

No new slugs to register (bounded-window-tournament excluded per above; all four built
slugs already in the population from round 1).

### Diversity check

Three live framings remain, genuinely distinct in mechanism: (1) direct constructive
phase-induction on the active set with an explicit stopping criterion
(jacobsthal-covering-bound), (2) finite-state residue-pigeonhole on the accepted sequence
(active-set-stabilization), (3) finite-state periodicity of the complement set B
(state-compactness-pigeonhole). All three still bottleneck on essentially the same core
fact (a self-sufficiency/termination lemma for the active prime set), which is the
problem's real difficulty, not a diversity failure — per the round-1 rule, convergence on
one hard lemma from genuinely different attack angles is expected, not a red flag. What
IS a red flag: growth-rate-contradiction has contributed no independent mechanism in two
rounds; the population would benefit from a genuinely different framing next round (e.g.
an explicit density/Jacobsthal-function-style closed-form bound, or the profinite/
compactness framing the outliner deliberately kept in reserve) if the current three stall
another round on the same lemma.

build set: jacobsthal-covering-bound, active-set-stabilization, state-compactness-pigeonhole
