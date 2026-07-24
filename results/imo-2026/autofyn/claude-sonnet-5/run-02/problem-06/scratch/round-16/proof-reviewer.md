# Round 16 proof-reviewer report — imo-2026-06

Reviewed all three built approaches independently from scratch. Verdicts below are
per-approach and independent of each other, per CLAUDE.md's routing rules.

## 1. even-a1-full-periodicity-theorem — APPROVE (Status: solved, scoped)

**Claim.** If `2 | a_1`, then `a_n = a_1 + 2(n-1)` for every `n ≥ 1`, so `T=1, L=2`
witness the problem's conclusion literally (not just eventually).

**Independent re-derivation.** Strong induction on `n`.
- Base `n=1`: trivial.
- IH: `a_i = a_1+2(i-1)` for `i ≤ n`, so every `a_i` (`i≤n`) is even (sum of two
  even numbers, since `a_1` even by hypothesis).
- `a_n+1` illegal: consecutive integers are coprime, `gcd(a_n+1,a_n)=1`, fails the
  `i=n` instance of legality. This half needs no evenness at all — I confirmed it
  independently, it's the elementary "consecutive integers coprime" fact.
- `a_n+2` legal: it is even (sum of two evens: `a_n` even by IH, `2` even), so
  `gcd(a_n+2, a_i) ≥ 2` for every `i ≤ n` (all `a_i` even by IH). This is exactly
  right — no case is skipped, the argument covers ALL `i ≤ n` simultaneously with a
  single shared prime `2`.
- Minimality: since `a_n+1, a_n+2` are the two smallest candidates > `a_n` and are
  consecutive integers (nothing strictly between them), illegal-then-legal forces
  `a_{n+1} = a_n+2` exactly, by the problem's own definition of `a_{n+1}` as the min
  of the legal set. I re-derived this "sandwich" argument from scratch — it is correct
  and the file even spells it out fully (not hand-waved).
- This closes the induction (`a_{n+1}` even too), completing it for all `n`.

**Independent computational check.** I reimplemented the greedy sequence generator
from scratch (trial-division gcd loop, no shortcuts) and ran it on 12 even seeds,
including several non-prime-power composites not in the builder's own list
(`194 = 2·97`, `2310 = 2·3·5·7·11`), plus the builder's own reported list. All 12
give consecutive-difference set `{2}` exactly, matching Theorem A on every sampled
prefix (60 terms each). Exact match, no discrepancy.

**Scope check (the crux of this review's mandate).** The file's Status header and
its dedicated "Precise scope" section explicitly state: (a) Theorem A is `solved`
ONLY for the restricted `2 | a_1` subfamily; (b) it says nothing about odd `a_1`;
(c) it does not use, and cannot be bootstrapped from, any part of the FAH/
persistent-type machinery elsewhere in the workspace; (d) the workspace-level
Status of the general problem correctly stays `partial`. I checked this is not an
overclaim in either direction: the induction genuinely uses `2 | a_1` in an
essential way (Claim 2's "every `a_i` is even" step is false for odd `a_1` — there
is no analogous single always-present prime), and the file does not, anywhere,
claim to extend beyond `2 | a_1`. This is a correctly-scoped, non-overclaiming
`solved` for a genuine infinite subfamily (strictly larger than the previously
certified `|Q|=1` power-of-2 special case — I confirmed `30 = 2·3·5`, a seed with
`|Q|=3`, is covered by this theorem but not by the old `|Q|=1` result).

**No skipped cases, no hand-waving, no circularity.** The two-candidate dichotomy is
exhaustive because `a_n+1, a_n+2` are literally the two smallest integers above `a_n`
and nothing lies between them; both directions (illegal / legal) are proved, not
assumed.

**Verdict: APPROVE.** This is a complete, gap-free proof of its own stated (and
correctly scoped) target. Certified as
`results/imo-2026-06/lemmas/even-seed-literal-periodicity-theorem.md`. The builder's
own Status header wording ("solved (for the restricted subfamily 2 | a_1 — ...
workspace-level Status ... remains partial)") is accurate and not an overclaim; the
overall `current.md` Status correctly stays `partial`, this does not flip the
problem to solved.

## 2. n1-periodicity-reconciliation — CHANGES REQUESTED (Status: partial)

**Claim.** A "Master Conditional Theorem": given two precisely-stated hypotheses
(H1) FAH at the terminal absorption-chain core, (H2) termination of the absorption
chain, the problem's full conclusion follows, via six already-certified lemmas
chained together with no new gap. Plus a genuine unconditional corollary (H1
trivializes when `2|a_1`) and an honest negative finding (H2 does not trivialize the
same way).

**Independent re-derivation of §2 (the chaining).** I checked each citation:
Free Facts → Persistent-Type Pigeonhole → Finite Core Theorem → Extended
Persistent-Type Pigeonhole (generic at any finite core, previously confirmed in
round 14's review) → Self-Absorbing Core Theorem (certified round 14, its own proof
gap closed and independently re-verified in that round) → Universal Early
Intersection Lemma + Literal n=1 Periodicity Theorem (certified round 15,
independently re-verified in that round, including a fresh re-simulation on
`a_1=175`). The §2 proof itself is one paragraph: "by H2 + Termination Criterion
Lemma the chain reaches a fixed point S*; by H1, FAH holds at S* (literally what H1
says); apply Literal n=1 Periodicity Theorem's two hypotheses (S* self-absorbing,
FAH at S*) directly." This is a genuinely correct, non-circular chaining — I traced
each hypothesis of the Literal n=1 Periodicity Theorem back to H1/H2 and found no
gap or hidden step. No load-bearing NEW mathematical claim is smuggled in; §2 is
pure legitimate reuse of prior certified content, correctly scoped as "assembly, not
new content."

**Independent re-derivation of §4.1 (Vacuous FAH under `2|a_1`).** Uses the Uniform
Evenness Lemma (2 | a_1 ⟹ 2 | a_n for all n, an immediate byproduct of the sibling
approach's induction) plus `2 ∈ Q ⟹ 2 ∈ S` for any core `S ⊇ Q`. Then `2 ∈ ρ_S(n)`
for every `n`, so every two elements of `𝒫'(S)` (each realized by some `n`) share
`2`. I re-derived this from scratch — correct, one line, no gap. Correctly claims
only "H1 trivializes," and correctly does NOT claim H2 trivializes.

**Independent check of §4.2 (H2 does not trivialize).** The obstruction identified —
self-absorption requires `P(a_j) ⊆ S` for the ENTIRE factorization of each early
term `a_j`, `j ≤ N(S)`, not merely a shared prime — is correct by the definition of
self-absorption in the certified Self-Absorbing Core Theorem. I checked this
definition matches what's used elsewhere (it does) and confirmed no argument using
only "`2` is shared" can force full-factorization containment of an arbitrary early
term's OTHER prime factors into a bounded core. This is a genuine, non-overclaimed
negative finding, correctly distinguished from a resolution attempt.

**No overclaiming found.** Status header says `partial`; "What is NOT claimed"
section explicitly disclaims resolving the general problem; H1/H2 are both honestly
flagged as open with their attempt histories cross-referenced accurately (17+
dead FAH mechanisms — I did not recount all 17, but the workspace's rounds 6-15
audit trail, which I spot-checked in `run_state.md`/`current.md`'s history, is
consistent with this count).

**Verdict: CHANGES REQUESTED** (Status `partial` — genuine, real progress:
the general problem is now expressed as a clean two-hypothesis conditional with a
fully gap-free reduction chain, a strict improvement in clarity/completeness over
prior rounds' more scattered framing, but H1 and H2 both remain open). The
"Vacuous FAH under 2|a_1" corollary is low-value (subsumed by approach #1's
stronger unconditional result for the same subfamily) but is correct; recorded as a
minor certified addendum, not a separate headline lemma file (kept in-file /
cross-referenced, matching the file's own framing).

## 3. core-growth-monotonicity — CHANGES REQUESTED (Status: partial)

**Claim.** Two new lemmas about how the exceptional-index threshold `N(S)`
(governing when the `S`-extended type stabilizes into a persistent type) behaves
under adjoining one prime `p` to a core `S`: the Binary Refinement Lemma (persistent
types split into at most two sub-types under core refinement) and the Threshold
Recursion Bound Lemma (`N(S∪{p}) ≤ max(N(S), max_B M_B)`, an exact one-prime
recursion). Then Proposition 3 shows the resulting `M_B` quantities are themselves
non-constructive from bounded prefix data — i.e. the recursion does not, by itself,
close sub-gap H2 (core-absorption-chain termination).

**Independent re-derivation, Binary Refinement Lemma.** `S' = S ⊔ {p}` (disjoint
since `p ∉ S`) gives `ρ_{S'}(n) = ρ_S(n) ∪ (P(a_n)∩{p})`, which is `ρ_S(n)` or
`ρ_S(n)∪{p}` according to `p ∤ a_n` / `p | a_n` — I re-derived this trivially from
the definition. (a) if `X` is `S'`-persistent (infinite occurrence set `I_X`), every
`n ∈ I_X` has `ρ_S(n) = X ∩ S` (by intersecting the display with `S`), so `X∩S` is
`S`-persistent (infinite `I_X` witnesses it). (b) for `S`-persistent `B` (infinite
`I_B`), partition `I_B = I_B^0 ⊔ I_B^1` by `p ∤ a_n` / `p | a_n`; since a finite ∪
finite union is finite, `I_B` infinite forces at least one part infinite — I
verified this pigeonhole step is airtight (no hidden assumption). Correct, no gap.

**Independent re-derivation, Threshold Recursion Bound Lemma.** For `n > N(S)`,
`B := ρ_S(n) ∈ 𝒫'(S)`. Three cases on which of `I_B^0, I_B^1` are infinite —
I checked all three are exhaustive (Binary Refinement Lemma guarantees at least one
infinite) and disjoint (can't have both "I_B^0 infinite, I_B^1 finite" and vice
versa). In each case I re-derived the conclusion (either `ρ_{S'}(n)` is always in
`𝒫'(S')` — case both infinite — or it's in `𝒫'(S')` except for the bounded-index
tail `n ≤ M_B` — cases (ii)/(iii)). The key sub-step ("the occurrence set of
`B∪{p}` at `S'` is contained in `I_B^1`, hence finite when `I_B^1` finite") is
correctly justified via the second display (`ρ_{S'}(n)∩S = ρ_S(n)`). No gap found;
the resulting bound `N(S') ≤ max(N(S), max_B M_B)` follows correctly by taking the
max over all exceptional indices.

I also ran a sanity computation (`a_1=175`, cores `S={2,3,5,7}`, `S'=S∪{13}`) using
a crude heuristic persistence-detector; it qualitatively confirmed the expected
partition-into-two-infinite/one-finite-part structure for several base types (e.g.
`{3,5}` and `{2,7}` show `I_0=0, I_1>0` patterns, i.e. one part identically empty in
the sampled window) — this is not a rigorous verification of the lemma itself (my
detector is a heuristic, not the certified definition) but is consistent with the
mechanism described and with the round's own report that `N(S_k)`-type quantities
show no sign of stabilizing within thousands of sampled terms.

**Independent check of Proposition 3 (Non-Constructivity of `M_B`).** The "two
consistent extensions" argument (fix any finite prefix up to `K`; extension (A)
makes `I_B^1` infinite from `K` on; extension (B) makes `I_B^1` finite but with the
single further occurrence pushed arbitrarily far past `K`) is a standard,
correct diagonalization-style argument that no function of a bounded prefix can
determine which of "eventually always" / "one more late occurrence" holds. I
confirmed this is essentially a general, TOOLKIT-INDEPENDENT fact about infinite 0/1
sequences (not really contingent on "no certified tool in this workspace does X" —
matching the round-10 Rule's distinction between portable logical principles and
workspace-contingent meta-claims), which strengthens rather than weakens its
standing as real content; I noted this distinction explicitly in the certified
lemma file and in current.md, since the file's own wording ("by any certified tool
currently in the workspace") slightly undersells the generality of what it proved.

**Overclaim check.** The Status header and body honestly report H2 as unresolved,
correctly distinguish "exact new recursion" (genuine progress) from "resolution"
(not claimed), and correctly do not fold the `math-explorer-termination.md`
15,000-term non-stabilization observation into a false proof of unboundedness (it
is cited only as consistent numerical corroboration of the now-proven structural
obstruction, not as evidence on its own).

**Verdict: CHANGES REQUESTED** (Status `partial` — two new correct, unconditional,
reusable lemmas; a real, rigorously-proved obstruction (not just an empirical
stall) narrowing what any future H2 attempt must supply; H2 itself remains open).
Certified as `results/imo-2026-06/lemmas/binary-refinement-and-threshold-recursion.md`.

## Lemma certification summary

- `results/imo-2026-06/lemmas/even-seed-literal-periodicity-theorem.md` — NEW,
  certified (from `even-a1-full-periodicity-theorem`). Includes the Uniform
  Evenness Lemma byproduct (used by `n1-periodicity-reconciliation` §4.1).
- `results/imo-2026-06/lemmas/binary-refinement-and-threshold-recursion.md` — NEW,
  certified (from `core-growth-monotonicity`; Binary Refinement Lemma + Threshold
  Recursion Bound Lemma). Proposition 3 (Non-Constructivity of `M_B`) recorded as a
  standing caution inside the same file rather than a separate lemma file, per the
  round-7 Lemma F / round-10 precedent for diagnostic (not machinery) content —
  though noted as arguably toolkit-independent, still kept in-file since it is
  specific to the `M_B` object introduced this round, not yet needed elsewhere.
- No lemma certified from `n1-periodicity-reconciliation` as a new standalone file
  this round: the Master Conditional Theorem is pure assembly of already-certified
  content (recorded prominently in `current.md`'s "Current best" as the canonical
  top-level conditional statement, per the file's own recommendation, rather than
  duplicated into a new lemma file); the Vacuous-FAH-under-`2|a_1` corollary is
  correct but low-value/subsumed, recorded in `current.md` rather than certified
  separately.

## `current.md` updates made this round

- Prepended a new round-16 `## Status` paragraph (all three approaches, verdicts,
  and lemma certifications) above the round-15 entry (history preserved below).
- Added three new bullets to `## Approaches tried` for the round-16 builds.
- Prepended a "Round 16 update" summary at the top of `## Current best` giving the
  current two-piece picture (2|a_1 fully solved; general case reduced to H1+H2),
  cross-referencing the fuller certified lemma stack, while preserving the
  round 1-4 historical snapshot below it for audit purposes.
- `## Full proof` unchanged (still absent — Status is `partial` at the workspace
  level; the even-a1 approach's own file carries its own scoped "Full proof").

## Overall workspace Status

Remains **partial**. This round's genuine progress: (1) the first outright APPROVE
of the run, for a real (if restricted) infinite subfamily, `2 | a_1`; (2) the
general problem's remaining content is now cleanly reduced to exactly two named,
precisely-stated, cross-referenced open hypotheses (H1=FAH, H2=core-termination)
via a fully gap-free chain; (3) H2 gained its first exact structural mechanism
(one-prime recursion) plus a rigorous proof of why the natural next step
(bounding `M_B`) is non-constructive — a real narrowing, not a restatement. FAH
(H1) itself remains untouched this round (by design) at 17+ confirmed-dead
mechanisms across 11 consecutive rounds (6-16).
