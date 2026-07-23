## imo-2026-03

### Headline finding (verify-before-trust catch): the round-9 "Core Open Lemma" / generalized
Full-Slack Insertion Lemma (`potential-weighting-upper-bound.md` §13.3, the statement the entire
§12.2 recursive-induction-on-`p` route depends on) is **FALSE at background size `|B|=2`**,
directly contradicting the file's own claimed "500/500 zero mismatches" in §13.4. This is a
decisive negative result, not a numerics artifact — see below for two independent codebases plus a
full hand-verification of a 4-element minimal counterexample.

### What I tried

Per dispatch, I implemented exact-integer brute-force versions of `OPT_σ(B,Z)` (unrestricted
DELETE/KEEP/MATCH selection, minimizing/maximizing `e`) and `TAGGED_σ(B,Z,s)` (same, restricted to
non-crossing selections that don't span split `s`) exactly as defined in
`potential-weighting-upper-bound.md` §11.1/§13.2, in **two independently-coded harnesses** (different
partition-generation algorithms), and cross-checked them against each other and against the file's
own worked example (`Y=(92,89,77,73)`, `INSERT_OPT(15,(89,73),2)=1` vs `INSERT_NC=15` — reproduced
exactly). All computation is exact Python `int` arithmetic on small instances (`q≤9`, `|B|≤2`), no
floats, no unbounded search — this directly follows the dispatch's three numbered ideas by first
building the machinery idea (2) and (3) need, then stress-testing idea (1)'s "closed form" question.

1. **Idea 1 (closed-form potential Ψ).** Computed `OPT(Y,p-1)` for many small `Y` (`p=1..5`) and
   inspected the winning selections. Found **no simple closed form**: winning selections mix
   KEEP/DELETE/MATCH in ways that depend on fine structure (e.g. `Y=(41,28,11)`: optimum `2` via
   `{MATCH(41,28)=13, KEEP(11)}`, not via any "delete-a-prefix-then-take-alternating-sum" family —
   the natural candidate `min_i e(Y[i:])` gives `11`, far from the true `2`). This rules out the
   simplest candidate closed forms; a genuine closed form, if one exists, is not a small variation
   of the existing telescoping/layer-cake identities. **Negative/inconclusive on idea 1** — not
   pursued further given the stronger finding below.

2. **Idea 2 (exchange/uncrossing on the full decomposition, not just MATCH).** At the *top level*
   (`|B|=0`, where `OPT=NC` is already known to hold in every tested case), enumerated ALL tied
   optimal selections of small `Y` (`p=4..6`, budget `p-1`) and measured the minimum number of
   index-role changes (K/D/M-membership, not just re-pairing within a fixed support) needed to get
   from a crossing-optimal selection to the *nearest* non-crossing-optimal one. Found distances of
   `2`–`4` role-changes even at `p≤6` (14 instances with both crossing and non-crossing optima
   tested) — this reproduces, rather than refutes, the already-documented dead end (memory rule
   #18/#26: local exchange fails because the global optimum changes *which* elements participate,
   not just how a fixed support is re-paired). **No new leverage found here**; consistent with, not
   contradicting, the population's existing diagnosis.

3. **Idea 3 (LP/TU).** Not pursued in depth — `e`'s dependence on a selection is through the
   *sorted rank* of the produced values, which itself depends combinatorially on the selection
   (values move rank depending on which matches/deletes are chosen), so the objective is not a
   fixed linear functional of a 0/1 selection vector in any of the natural encodings I could see
   quickly; a genuine LP relaxation would need a good compact formulation of "produce a sorted
   alternating sum," which isn't apparent. Flagging as **unpromising without a much longer look**,
   not ruling it out definitively.

4. **Direct construction/verification (this ended up being the main finding).** Built the exact
   `OPT_σ`/`TAGGED_σ` machinery §13.2 defines, and used it to (a) reproduce the file's own §11.3
   counterexample exactly, then (b) test the file's own §13.4 claim ("`|B|=2`: full three-branch
   decomposition reproduces the true `OPT`/`TAGGED(·,0)` values exactly, `500/500`, zero
   mismatches") with a **fresh, independent** random sweep.

### The counterexample (decisive, triple-verified: 2 independent codebases + hand)

**Minimal example**, found by small exhaustive search over `q≤4`, `B`-entries `≤14`:
```
B = {2, 4},   Z = (6, 3, 2, 1)  (q=4, |B|=2)
OPT_{+1}(B,Z)        = 0   (via crossing match: MATCH(z_1=6,z_3=2)=4, MATCH(z_2=3,z_4=1)=2,
                             giving multiset {2,4} ∪ {4,2} = {4,4,2,2}, e = 4-4+2-2 = 0)
TAGGED_{+1}(B,Z,0)   = 1   (this is the ONLY way to produce {4,2} as the extra values — 4 can only
                             come from 6-2, and once index 2(value 2) is used there, the second "2"
                             can only come from MATCH(3,1); these two arcs (0,2) and (1,3) cross
                             (0<1<2<3) — every non-crossing alternative gives e≥1, confirmed by
                             exhaustive check of all 5 candidate non-crossing/keep/delete
                             combinations)
```
So `OPT_{+1}(B,Z) = 0 \ne 1 = TAGGED_{+1}(B,Z,0)` — a clean, fully hand-verifiable failure of the
generalized Full-Slack Insertion Lemma at `|B|=2`.

**Verified two more ways:**
- A fresh random sweep replicating §13.4's own methodology as closely as possible (`q=2..7`,
  integer entries up to `300`, `|B|=2`, `500` trials): **22/500 mismatches (4.4% failure rate)**,
  not `0/500` as the file claims. Two independent codebases agree exactly on every mismatch found
  (cross-checked on 2 examples digit-for-digit).
- **Reachability check** (so this isn't dismissible as "unrealistic `B`"): simulated genuine
  2-level top-down MATCH peeling on real random lists `Y` (`p=7..9`) — i.e. `B`'s two elements are
  actual differences `y_1-y_{k_1}` then `z_1-z_{k_2}` produced by a real recursive peel, not
  arbitrary numbers — and still found **5/300 failures (~1.7%)** among reachable `(B,Z)` states,
  e.g. `Y=(40,40,34,31,26,24,21,15,7)`, background differences `(14,16)`, residual `Z=(34,31,21,15,7)`:
  `OPT=0` vs `TAGGED(·,0)=1`.
- **Sanity control (rules out a systematic bug):** the same two codebases, on the same kind of
  sweep, find **zero failures at `|B|=0` (400 trials) and `|B|=1` (400 trials)** — exactly matching
  every prior round's independent verification of the top-level `OPT(Y,p-1)=NC(Y,p-1)` claim and
  the narrow (`|B|≤1`) Full-Slack Insertion Lemma. The failure is precisely localized to `|B|≥2`,
  the genuinely-recursive regime — consistent with, and sharpening, round 9's own observation that
  `|B|=2` is "the smallest genuinely-recursive instance," except round 9's own harness apparently
  missed the failures its own methodology should have found.

### Diagnosis — why `|B|=2` breaks (a concrete lead for a new technique)

The generalized `TAGGED_σ(B,Z,s)` formalism treats the background `B` as a **flat multiset of
values with no memory of the original indices/arcs that produced them**. At `|B|\le1` this loses
nothing (Fact 3 / the General Rank-Extraction Identity only need `B`'s *values*, not their
provenance, to compute a sign-and-offset). But at `|B|\ge2`, the *crossing relationship between the
two background-generating arcs themselves* (and between a background arc and a current match in
`Z`) is exactly the information the flat-set abstraction discards — and the minimal counterexample
above is precisely a case where the winning `OPT` selection needs two arcs, `(6,2)` and `(3,1)` in
original-index terms, that cross each other; nothing in the `TAGGED_σ(B,Z,s)` framework can express
"these two background-producing arcs already cross" because `B` no longer remembers they came from
arcs at all.

**Concrete new-technique lead for the outliner:** the correct generalization of the peeling
induction must carry **positional/index history for every background element** (e.g. tag each
background value with the interval of original indices its generating arc spanned, and forbid new
matches from crossing *any* previously-recorded arc, background or not — not just the current
`Z`'s own split `s`), rather than the current "flat value set" `B`. This is a strictly more complex
bookkeeping (a genuine non-crossing partition *history*, not a single split point) but it is the
only way I found to avoid discarding exactly the information whose loss causes the counterexample.
Concretely: redefine the induction's invariant as a **fully non-crossing-tagged recursive
state** — the background isn't a flat set, it's itself a partially-built non-crossing partition —
and re-derive the DELETE/KEEP/MATCH branch bijections in this richer state space. I did **not**
attempt this construction (out of scope for an explorer — it's a real skeleton-level task for the
outliner/builder), but the counterexample above pins down exactly the phenomenon it needs to
handle, and suggests the fix is architectural (change what is carried forward), not a stronger
inequality to prove within the current framework.

**Alternative reading (equally worth flagging):** since the failure needs `|B|\ge2`, and the actual
top-level target only ever has `|B|=0`, it's possible the cleanest fix is to **abandon the
recursion-in-background-size approach entirely** (§12.2's whole skeleton) and instead seek a
genuinely global/non-recursive argument for `OPT(Y,p-1)=NC(Y,p-1)` directly on the original `Y` —
consistent with round 9's own honest observation that the recursive route "provides no independent
reduction in difficulty," now sharpened to "and, moreover, is provably false once you try to run it
two levels deep in its stated form."

### Cheap-kill candidates
- **Immediate cheap kill for any future proof draft:** before trusting any inductive step that
  generalizes `B=\emptyset`/`|B|\le1` machinery to arbitrary background size, test it at the minimal
  instance `B=\{2,4\}, Z=(6,3,2,1)` above — it is small enough to hand-check in under a minute and
  already refutes the naive generalization.
- Parity/size check: `|B|=0,1` hold unconditionally (0 failures across 800+ trials combined,
  multiple rounds); `|B|\ge2` fails at a `~2-5\%` rate — this crisp threshold (not a gradual
  degradation) is itself useful signal that whatever breaks is a genuinely combinatorial
  (crossing-among-background-arcs) phenomenon, not a numerical edge effect.

### Candidate technique(s)
- The positional/history-carrying generalization of the Peeling Lemma described above (untried,
  concrete, would need real construction work).
- Failing that, a **direct, non-recursive** argument for `OPT(Y,p-1)=NC(Y,p-1)` (e.g. an injective
  charging map, as the still-untried `aimo-0558`-style lead in §12.3 already proposes) is now
  *more* motivated than before, since the recursive route is shown to need strictly more than "the
  same lemma at every level" — it needs a lemma the current formalism can't even state correctly.

### Knowledge-base entries to use
- `lemmas/general-rank-extraction-identity.md`, `lemmas/insertion-and-cascade-facts.md` (Fact 3/5),
  `lemmas/layer-cake-and-noncrossing-independence.md` — all still valid and reusable (my finding
  doesn't touch their correctness, only the further generalization built on top of them in
  `potential-weighting-upper-bound.md` §12–§13).
- No new knowledge-base entry is proposed this round; this is a diagnostic/negative finding.

### Analogous past problems (cruxes)
Not re-searched this round (dispatch was a direct-computation lens on one specific open lemma, not
a fresh corpus search) — see prior rounds' crux findings (`aimo-0558` charging argument, already on
file as an untried fallback in §12.3; `aimo-0287`/`aimo-0298`/`aimo-0019` from round 4, transferable
proof shapes for non-local obstructions). None of these obviously address the specific
"positional-history" fix identified above; if a future round wants a crux for it, search for
"nested/tagged non-crossing partition" or "arc-history-preserving induction" subtopics.

### Prior progress
`potential-weighting-upper-bound`'s round-9 unification (Match-Recovery Lemma / generalized
Full-Slack Insertion Lemma) is the current top of the population for the upper-bound gap — see
above for why its central open lemma is now known to be **false as stated**, not just unproved.

### Dead ends (do not retry)
- **NEW (this round): do not attempt to prove the generalized Full-Slack Insertion Lemma /
  Match-Recovery Lemma / `FSI(q)` for arbitrary flat background `B` with `|B|\ge2`, in the form
  stated in `potential-weighting-upper-bound.md` §13.2–§13.3.** It is FALSE — minimal
  counterexample `B=\{2,4\}, Z=(6,3,2,1)`, `OPT_{+1}=0 \ne 1=TAGGED_{+1}(\cdot,0)`, verified by two
  independent codebases and by hand; also fails on `~2-5\%` of both arbitrary-`B` and
  genuinely-reachable-`B` random instances at `|B|=2`. **This means §12.2's entire recursive
  strong-induction-on-`p` skeleton, as currently framed (flat growing background), cannot be
  completed — it is not merely stuck, it needs restructuring (see Diagnosis above) or replacement
  by a non-recursive argument.**
- Reconfirmed (not new): local pairwise/few-index exchange arguments that hold the support mostly
  fixed do not find a short path from a crossing-optimal to a non-crossing-optimal top-level
  selection (distances `2`–`4` even at `p\le6`) — consistent with the existing round-6/round-9 dead
  ends on this family, not a new finding.
- Do NOT re-flag idea 1 (closed-form potential Ψ) as promising without new structural insight — the
  simplest candidate closed forms (prefix-deletion alternating sums) are off by large margins on
  concrete small examples.

### Small-case / intuition notes (labeled as conjecture / diagnosis, not proof)
- Conjecture (well-supported, unchanged): the TOP-LEVEL claim `OPT(Y,p-1)=NC(Y,p-1)` (`|B|=0`)
  itself still appears true — 400/400 fresh trials this round, consistent with 2000+ in prior
  rounds. My finding does **not** threaten the truth of the theorem's target, only the specific
  recursive proof strategy currently being pursued for it.
- Diagnosis (new, reasonably confident): the reason `|B|\in\{0,1\}` are "easy" and `|B|\ge2` is
  hard is that a single external point's rank/sign relative to a sorted list is a *scalar* fact
  (Fact 3/Rank-Extraction handle it exactly), but two-or-more external points can have a *mutual*
  crossing relationship with each other and with the residual list that a flat multiset
  representation cannot see — this is a structurally different (harder) kind of fact, not just "a
  bigger case of the same fact." This reframes why the round-9 "unification" into one Core Open
  Lemma, while a real and correct piece of bookkeeping, was unification into a lemma that turns out
  to be false, not merely hard — the outliner should treat this as redirecting effort toward either
  the positional-history fix or a wholly non-recursive top-level argument, not toward "try harder
  at the same generalized statement."
