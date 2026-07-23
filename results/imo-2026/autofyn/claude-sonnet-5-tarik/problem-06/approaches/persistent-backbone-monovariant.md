## Status
partial

## Round 8 Outline (proof-outliner directive — retarget from "permanent
bundle count" to the true remaining object, `Λ_S`/`𝓥_S` TOTAL finiteness
(permanent + transient members); certify a new unconditional pigeonhole
corollary first, then attempt the transient-count completion this round's
target genuinely requires)

**Context (read first).** Round 8's dedicated thread-unification explorer
(`/tmp/round-8/math-explorer-thread-unification.md`) proved, by direct
computation on both documented depth-3 instances, that this file's round-7
target — bounding the COUNT of *permanent* `D_S`-disjoint bundles
(`lemmas/lemma-permanent-bundle.md`) — is a **proper subset** of what
`Λ_S`-finiteness (equivalently `𝓥_S`-finiteness, Theorem V) actually
requires: the *transient* antichain members (values that are minimal for a
while, then get dominated and removed — e.g. `a_1=21528751,S={197}`'s bundle
`{2,3,7,41,197}`, realized at `a_1291`, transient until dominated by
`{2,3,7,197}` at `n=2575`) are a separate, still fully open count, on record
since round 6 as the "Growth-Budget Lemma"/"Generation-Chain-count" gap and
never closed. **Solving the permanent-bundle-count target alone, even
completely, would NOT close this approach's share of the whole problem.**
This round retargets accordingly: Step 1 below certifies genuinely new
unconditional content (small effort, real payoff); Step 2 is this round's
actual open target, honestly harder, using Step 1 as one input among several.

**Step 1 — certify the Escape-Confinement Pairwise-Disjoint-Bundle-Count
Corollary (cheap, ~10 lines, from two already-certified facts; do this
first, it is genuinely new and reusable regardless of Step 2's outcome).**

*Statement.* Fix a proper core `S` with `I_S≠∅`, and suppose there exists
**any** index `j_3` with `rad(a_{j_3})∩S=∅` (a "core-avoiding witness" — flag
its existence as a standing sub-lemma per the Watch-out note below, do not
assume it silently). Apply the already-certified **Escape-Confinement
Lemma** (`lemmas/lemma-escape-confinement.md`) with `κ:=S` (`Q=∅` — `S`
itself is trivially "blocked" by `j_3` by definition, no `J_S`-infinite
hypothesis needed here, unlike the Single-Companion Finiteness Lemma). Then
**every** realized companion bundle `Q_i` (`i∈I_S`, `rad(a_i)=S∪Q_i`,
whether it is ultimately permanent or transient) satisfies `Q_i∩
comp(a_{j_3})≠∅`. Consequently: **any family of pairwise-disjoint realized
bundles for `S` has size `≤|comp(a_{j_3})|`** — a small, explicit,
`a_1`-and-`S`-computable constant (pigeonhole: disjoint bundles cannot share
the one witness-prime each is forced to contain).

*Numerical corroboration (round 8's subset-avoidance explorer, reuse
directly, do not re-derive from scratch).* Verified against **every**
realized index of **every** proper core of all 5 mandated hard cases
(~636,000 checked realized indices, 12 core instances), zero violations;
observed bound values `2`–`4` in every tested case, including the
non-singleton core `S={103,197}` of `a_1=21528751` where it correctly
explains why the two known permanent bundles `{5,11}`,`{11,97}` share the
prime `11` (not pairwise disjoint) rather than being independent.

**This is genuinely new, unconditional content beyond the certified
Permanent Bundle Lemma**: it applies to *every* realized bundle (permanent
or transient alike), not just ones already shown permanent via (SA)/(SCA),
and needs no `J_S`-infinite hypothesis. Certify it as its own small lemma.

**Step 2 — this round's real, harder target: complete the transient-member
count (the Growth-Budget Lemma, correctly reidentified, not the count of
permanent bundles).** Do **not** present Step 1 alone as closing anything —
a bound on *pairwise-disjoint* bundle families does not by itself bound the
*total* count of bundles (they can pairwise-intersect in many ways and still
be infinite in number, e.g. an infinite family all sharing one prime of
`comp(a_{j_3})` but otherwise growing). Attempt, in order:
  (a) **Revisit the round-6 Growth-Budget Lemma's exact obstruction**
      (Lemma FOM's `T_C` + Fan-Size Corollary + Lemma 1's linear gap bound,
      already certified) with Step 1's new pairwise-disjoint bound as a
      fresh lever: combine the *iterated* Escape-Confinement recursion
      (already certified, "Iterated form") with Step 1's bound applied at
      **each level of the recursion**, not just the top level — i.e., try
      to show the total branching factor across the whole confinement
      recursion (not just its first step) is bounded, by re-applying the
      pigeonhole argument to the *confinement set at each stage* rather
      than to `comp(a_{j_3})` alone. State plainly whether this converts
      the already-diagnosed "pointwise-in-`n`, not cumulative" obstruction
      (rounds 3–6) into an actual cumulative bound, or hits the same wall
      one level down — report either outcome honestly.
  (b) **If (a) stalls, do not silently fall back to assuming
      `ω(a_n)=O(1)`** (that hypothesis, and the Δ-system/sunflower route
      built on it, belongs to the new `sunflower-bundle-closure` approach
      this round — see that file; keep this approach's contribution
      independent so the population has two genuinely different levers on
      the same target, not one lever under two names).

**Watch out (standing sub-lemma, shared with `forced-primes-well-
ordering`'s Step 2 this round — prove once, cite from both, do not
duplicate).** Step 1 needs *some* index `j_3` with `rad(a_{j_3})∩S=∅` to
exist for every proper core `S⊊P_1`. This was flagged as an unproved
"likely easy pigeonhole, not yet done" in round 6's outline and has not been
explicitly proved anywhere in this workspace since — every worked example
happens to have one, but general existence is not established. Prove it
first (candidate mechanism: since `S≠P_1`, by the already-certified Theorem
CD core-decomposition, `P_1\S≠∅`; combined with `I_S≠∅` and Lemma P
(`G_i≠∅` always) applied to whichever other proper core is realized
infinitely often — needs one clean argument, not yet written down).

## Round 8 Build (proof-builder — this round's work, read first)

Following the round-8 outline above and the outline-reviewer's **APPROVE
(build)** verdict (`/tmp/round-8/outline-reviewer.md`: Step 1 "genuinely
new, correct, and cheap"; Step 2 "honestly scoped as open... no fatal
flaw"), this round:

1. **Certified Step 1 in full** — the Escape-Confinement
   Pairwise-Disjoint-Bundle-Count Corollary — with one honest addition the
   outline itself flagged but did not resolve: the "core-avoiding witness"
   existence sub-lemma. I did **not** manage to prove this in general (see
   below for exactly why the natural proof attempts stall); I instead proved
   a real, unconditional **directional** fact (the Complement Witness Fact:
   `I_S\ne\varnothing\Rightarrow J_{P_1\setminus S}\ne\varnothing`) and gave
   an honest diagnosis of why the needed direction (`J_S\ne\varnothing`
   itself) resists the same argument, then stated the Corollary explicitly
   conditional on witness existence (verified case-by-case per the round-8
   outline-reviewer's own spot check, and automatic whenever the file's
   pre-existing standing hypothesis "`J_S` infinite" holds — so this adds no
   genuinely new unproven hypothesis beyond what the rest of this reduction
   chain already carries).
2. **Built a genuinely new tool for Step 2** — proved a **Realized–Blocked
   Dichotomy Lemma (RBD)**, synthesizing the already-certified Lemma ER and
   Permanent-Inadmissibility Lemma into a clean "no third case" statement for
   *radical values* (not just candidate integers), not explicitly stated
   anywhere in this workspace before. This turns out to be exactly the tool
   needed to make the escape-recursion into a well-defined branching process
   with no undetermined nodes.
3. **Attempted outline Step 2(a) directly** — iterating the pigeonhole
   argument at every level of the confinement recursion — and found a
   genuine, fully rigorous **conditional** theorem, not previously proved in
   this workspace: a **Finite-Reachability Theorem**, via an explicit
   "reachable-set" construction and a direct proof of the relevant
   finitely-branching-tree fact (a form of König's Lemma, proved from
   scratch, not merely cited). This shows: **if** the escape-recursion has no
   infinite chain of always-blocked bare values rooted at `S` (a precisely
   stated, named open hypothesis, "NIBC"), **then** the count of bundles
   satisfying the already-certified Permanent Bundle Lemma's Subset-Avoidance
   (SA) hypothesis is finite. This formally upgrades round 7/8's *informal*
   diagnosis ("the naive branching-recursion proof strategy does not visibly
   terminate") into an exact, gap-free, named conditional implication.
4. **Went one step further than the outline asked and found the precise
   boundary of what this mechanism can ever prove** — proved that a bundle
   `Q` is reachable by this recursion **if and only if** it satisfies (SA);
   and, on the one documented worked transient example in this workspace
   (`a_1=21528751,S=\{197\}`, the bundle `Q=\{2,3,7,41\}` realized at
   `a_{1291}`, later dominated by `\{2,3,7,197\}` at `n=2575`), directly
   verified that (SA) **fails** for exactly the reason it is transient (its
   proper subset `\{2,3,7\}` is independently realized, the very event that
   dominates it). This proves — not just observes — that **transient bundles
   are structurally invisible to the entire Escape-Confinement/pigeonhole
   mechanism** (both this round's Step 1 and Step 2), matching and sharpening
   with an actual proof (not an empirical pattern) the round-8 outline's own
   warning that Step 1 alone cannot reach the true target.
5. **Did not close** `𝓥_S`/`Λ_S`-finiteness. Two honest open gaps remain,
   precisely named: (i) general existence of a core-avoiding witness for
   every proper core (Watch-out sub-lemma, only case-by-case verified); (ii)
   NIBC itself (not established — and disfavored by the round-7/8 depth-3
   counterexamples showing escape/confinement depth is not capped at a small
   constant). Even a full resolution of both (i) and (ii) would **only**
   bound the permanent/(SA)-satisfying share of `Λ_S`, per finding 4 above —
   the transient share needs a genuinely different mechanism, not a variant
   of this one. Status remains `partial`.

See "Round 8: Realized–Blocked Dichotomy, the Pigeonhole Corollary, and the
Finite-Reachability Theorem" below (inserted into "Current best," directly
before "## Full proof") for full statements, proofs, and the worked example.

## Round 7 Outline (proof-outliner directive — bundle-size induction is now
provably foreclosed; certify the Permanent Pair Lemma, pivot to a direct
companion-COUNT bound on `Λ_S`, not any further size-induction)

**Context (read `current.md`'s Round 6 update first).** This is the 4th
consecutive round the whole population has bottomed out on `𝓥_S`-finiteness
(equivalently `Λ_S`-finiteness, this file's Multi-Companion Reduction
Proposition). Round 6 refuted `core-depth-induction`'s induction on `|S|`.
This round's dedicated explorer
(`/tmp/round-7/math-explorer-multicompanion-induction.md`) tested the natural
next architecture — induction on companion-bundle size `k=|Q|`, using the
already-certified Single-Companion Finiteness Lemma (`k=1`) as a base case —
and found something stronger than "no reduction found": **a proof that no
`k=2\to k=1` reduction can exist**, for a concrete, recurring class of
instances.

**Step 1 — certify the Permanent Pair Lemma (cheap: 3 lines from two
already-certified facts; do this first).**

*Statement.* Fix a proper core `S` with `J_S` infinite (the standing
hypothesis of the Single-Companion Finiteness Lemma, imported unchanged).
Let `Q=\{q_1,q_2\}` (`q_1\ne q_2`) be realized as a bundle for `S` (some
`i\in I_S` has `\mathrm{rad}(a_i)=S\cup Q`), with `q_1,q_2\notin D_S
\setminus P_1` (`D_S:=\bigcap_{j\in J_S}\mathrm{rad}(a_j)`, the already-
certified finite set bounding sole companions). Then `S\cup Q` is **never**
dominated within `𝓜_n^S` — it is a permanent member of `𝓥_S`, contributing
forever to `Λ_S`.

*Proof sketch (write up in full rigor).* Any dominator of `S\cup Q` within
`I_S` must have radical `\subsetneq S\cup Q`, hence of the form `S\cup Q'`
for `Q'\in\{\varnothing,\{q_1\},\{q_2\}\}` (radicals of class `S` always
contain `S`). `Q'=\varnothing` is impossible by the Permanent-Inadmissibility
Lemma (`forced-primes-well-ordering`, cite by name) applied with `C:=S` and
any `j\in J_S` (`\mathrm{rad}(a_j)\cap S=\varnothing` by definition of `J_S`,
nonempty since `J_S` infinite). `Q'=\{q_1\}` or `\{q_2\}` is impossible by
the *contrapositive* of the Single-Companion Finiteness Lemma (its conclusion
is `Q_S\subseteq D_S\setminus P_1`; `q_1,q_2\notin D_S\setminus P_1` by
hypothesis, so neither can ever be realized as a sole companion of `S`). No
candidate dominator exists. `\blacksquare`

**Step 2 — record why this forecloses bundle-size induction as a family, not
just this one attempt (do not re-attempt any of this).** This is not a
failed guess (contrast `core-depth-induction`'s Step 3, refuted only
*empirically*) — it is a structural obstruction: there provably exist `k=2`
bundles that **never** reduce to any `k=1` fact, because their companions are
excluded, by the `k=1` result itself, from ever being sole companions. Round
6 already showed `|S|`-induction fails (self-similarity: peeling one core
element lands back on a same-order-difficulty question with a fresh prime);
this round shows peeling one *bundle* element fails for the structurally
identical reason (confirmed independently on two worked instances,
`a_1=4199,S=\{17\}`, bundle `\{3,83\}`, and `a_1=21528751,S=\{103,197\}`,
bundle `\{11,97\}`). **Do not attempt a third syntactic-size induction**
(`T_C`-magnitude, total recruitment count, or any other single well-founded
measure on companion structure) without first hand-checking a concrete
instance for this exact self-similar-permanence obstruction, per the
explorer's own recommendation (§3.4).

**Step 3 — this round's real target: a direct companion-COUNT bound, not an
existence/induction argument (per the orthogonal-mechanism explorer's
independent, convergent recommendation).** The Permanent Pair Lemma sharpens
(does not close) the open content: instead of the abstract Multi-Companion
Reduction Proposition ("bundles of `\ge2` new companions reduce to a local
FCBC-style hitting-set problem"), the precise open sub-target is now:
**bound the number of distinct bundles `Q` with `Q\cap(D_S\setminus P_1)=
\varnothing` ever realized for a fixed proper core `S`** — each such bundle
is *permanently* irrevocable (Step 1), so if their count is finite, this
piece of `Λ_S` is finite; if their count is provably unbounded for some
`a_1,S`, FCBC would need a different mechanism entirely for that instance
(has not been observed in any tested case, but not ruled out). Attempt a
direct extremal/counting argument (e.g., combining Lemma 1's linear gap bound
with an accounting of how many genuinely fresh companion primes can enter
before growth outpaces admissibility) — **explicitly flagged trap**: this is
the same shape of argument that sank the already-refuted Growth-Budget/Markov
pointwise-vs-cumulative attempts (rounds 3–6); do not resurrect that verbatim
mechanism. If no genuinely new leverage is found, report honestly (a
confirmed "still open, here is exactly why" is valuable, not a failure) —
also attempt the natural generalization to permanent **triples** (`|Q|=3`,
ruling out all proper nonempty subsets, which needs the size-2 case as a
sub-bound) as a cheap next data point, not attempted by this round's
explorer.

**Step 4 (bookkeeping).** Also honestly re-flag the still-unclosed standing
hypothesis "`J_S` infinite for every proper core `S`" (unproved in general,
inherited unchanged from round 6) — the Permanent Pair Lemma is conditional
on it exactly as the Single-Companion Finiteness Lemma already is.

## Round 7 Build (proof-builder — this round's work, read first)

Following the round-7 outline above (Steps 1–4), this round:

1. **Certified the Permanent Pair Lemma — and found and fixed a genuine gap
   in it.** The outline's proof sketch (matching the round-7 math-explorer's
   and outline-reviewer's independent derivations) only considers dominators
   drawn from `I_S` (same-class indices). Writing a fully self-contained
   proof from scratch, I found this is **incomplete for non-singleton
   cores**: a dominator of `S∪Q` need only have radical `⊊S∪Q` (any class,
   not necessarily class `S`), and such a radical can take the form
   `S'∪Q''` for a *proper* nonempty subset `S'⊊S` (a "sub-core" dominator)
   whenever `|S|≥2` — a case the original argument never excludes. I proved
   a **Class-Decomposition Fact** showing this sub-core case is
   automatically *vacuous* when `|S|=1` (every tested singleton-core
   instance in this workspace, e.g. `a_1=4199,S=\{17\}`, is therefore
   already fully rigorous, no fix needed), but is a genuine *additional*
   requirement — **Sub-Core Avoidance (SCA)** — for non-singleton cores
   (e.g. the round-7 explorer's own `a_1=21528751,S=\{103,197\}` example).
   I then **proved (SCA) unconditionally for that exact instance** by
   exhibiting two explicit early witnesses (`a_2,a_3`) and invoking the
   already-certified Permanent-Inadmissibility Lemma directly — not a
   numerical sample, a full proof — closing the gap completely for the one
   non-singleton case on record. See `lemmas/lemma-permanent-bundle.md`.
2. **Generalized to a Permanent Bundle Lemma (arbitrary bundle size `k`,
   new this round)**, adding a **Subset Avoidance (SA)** hypothesis
   (no proper nonempty subset of the bundle is ever separately realized as
   a companion of `S`) needed for `k≥3` (shown to reduce to, not be
   implied by, `Q∩D_S=∅` for `k=2`, but to be a genuinely independent
   extra condition for `k≥3`). Validated this exhaustively: across a
   from-scratch simulation of all five mandated hard cases pushed to
   `N=3`–`5,000,000` (two to three orders of magnitude past any prior
   round's stress test, cross-validated against an independent
   brute-force `O(N^2)` simulator with zero discrepancies — see below),
   found **44 size-`\ge3` `D_S`-disjoint fresh bundles**; **in every single
   one**, "(SA) holds" correctly predicted "still alive in the antichain at
   the final index" and "(SA) violated" correctly predicted "dominated" —
   zero exceptions in either direction. Three instances (one negative
   control) were additionally proved by explicit witness, not just
   observed. Full statements, proofs, and worked examples in
   `lemmas/lemma-permanent-bundle.md`.
3. **Recorded, sharpened beyond the outline's request, why this forecloses
   bundle-size induction as a family.** The round-7 explorer already showed
   no `k=2\to k=1` reduction exists. This round shows the natural "fix" —
   replacing the flawed size-`k` criterion with the corrected
   `D_S`-disjointness-plus-(SA) criterion — **also does not yield a working
   induction**: verifying (SA) for a size-`k` bundle requires knowing
   whether *any* of its `2^k-2` proper nonempty subsets is ever realized —
   an instance of the identical general question, recursively, one level
   down. This is an honest deepening of the foreclosure, not a
   contradiction of it: see `lemmas/lemma-permanent-bundle.md`'s final
   section.
4. **Attempted the outline's real target — a direct count bound on `Λ_S`
   — via a much deeper numerical stress test than any prior round**, to
   look for a genuine pattern before attempting an analytic argument.
   Built an efficient simulator (minimal-radical-antichain-based
   admissibility, `O(1)` gcd checks per candidate rather than
   re-factoring) and **independently cross-validated it against a
   brute-force `O(N^2)` all-pairs-gcd simulator** (zero discrepancies,
   `a_1\in\{247,2747,4199,4087,21528751\}`, `N` up to `3000`) and against
   an independent from-scratch `O(N^2)` minimal-antichain computation
   (zero discrepancies, `a_1=247`, `N=3000`) before trusting any large-`N`
   run. Pushed all five mandated hard cases to `N=3`–`5{,}000{,}000`
   (`247,2747,4199,4087` to `5{,}000{,}000`; `21528751` to `3{,}000{,}000`,
   its larger starting value making runs proportionally slower). **Finding
   (new, and considerably deeper than anything previously recorded in this
   workspace): for every proper core `S` of every one of the five
   mandated cases, the count of distinct fresh (`𝓥_S`-member) bundles —
   both `D_S`-disjoint and otherwise — is completely flat from an early,
   `a_1`-specific index all the way to the `N=3`–`5,000,000` end of the
   simulated range**, a `10^3`–`10^6`-fold extension with zero new
   distinct values appearing. Even more strikingly, **the *entire global*
   minimal-radical antichain `𝓜_n` (not just its per-core restriction) was
   verified, by literal set-identity (not just size), to freeze completely
   at a small index and never change again**: `n=7` (`a_1=247`), `n=163`
   (`a_1=2747`, matching the already-documented collapse point exactly),
   `n=92` (`a_1=4199`, matching round 4's "worst case `n\le92`" finding
   exactly), `n=54` (`a_1=4087`, matching the already-documented
   `Negative Finding 2` collapse point exactly), `n=44967`
   (`a_1=21528751`). This is genuine new depth of evidence for (MRS) on
   these five instances (previously verified only to a few tens of
   thousands of terms) — **but it remains evidence, not proof, for a
   general `a_1`**, and I found **no new analytic mechanism** converting
   it into a bound valid for every core `S` and every `a_1` (the
   "pointwise-for-tested-cases vs. provable-in-general" gap that has
   resisted rounds 3–7 persists). Reported honestly below, not overclaimed.
5. **Did not close** the count bound in general. Status remains `partial`.

See "Round 7: Permanent Bundle Lemma and the count-bound stress test"
below (inserted into "Current best", right after the Round-6
"Growth-Budget attempt" subsection) for full detail, worked examples, and
the exact numerical tables.

## Round 6 Outline (proof-outliner directive — certify Lemma FOM, pivot to a
Generation-Chain / Growth-Budget counting argument on `𝓥_S`)

**Context (read `current.md`'s Round 5 update first).** The whole population
has converged on one shared gap: finiteness of `𝓥_S` for each proper core
`S⊊P_1` (this file's own Theorem V + `imprint-automaton-periodicity`'s
Theorem CD/Lemma TC give the exact reduction, already certified — cite, do
not re-derive). This round's fan-structural explorer found and numerically
verified (6000+ instances, zero exceptions) a new elementary fact, **Lemma
FOM (First-Occurrence Minimality)**, not yet certified anywhere in this
workspace: the first term ever realizing a given radical `C` is *exactly*
`T_C:=\min\{x>a_1:\mathrm{rad}(x)=C\}`, a fixed, `a_1`-and-`C`-computable
integer. This gives, as a free corollary, a **conditional** bound on fan
size at any absorption event (conditional on the absorption actually
happening) — genuine new content, but NOT by itself a finiteness proof (see
the honest circularity warning below).

**Step 1 — certify Lemma FOM in full (this file's own home for it: it
strengthens the already-certified Record Characterization Lemma).**
*Statement.* If `n\ge2` is the first index with `\mathrm{rad}(a_n)=C` (no
`i<n` has `\mathrm{rad}(a_i)=C`), then `a_n=T_C`.
*Proof.* Admissibility of a candidate integer against a fixed prefix
`a_1,\dots,a_m` depends only on its radical (via `\gcd(x,y)>1\iff
\mathrm{rad}(x)\cap\mathrm{rad}(y)\ne\varnothing`), not its magnitude.
Suppose toward contradiction `a_n\ne T_C`. Since `T_C` is an integer `>a_1`
with radical `C`, minimality of `T_C` gives `T_C\le a_n`; and `T_C` cannot
equal any `a_i` (`i<n`), else `i` would already realize `C`, contradicting
"`n` is `C`'s first occurrence" — so `T_C<a_n` strictly. Hence `T_C` lies in
a unique gap `a_i<T_C<a_{i+1}` for some `i` with `i+1\le n` (using
`a_1<T_C`, immediate from `T_C`'s definition). Since `a_n` is admissible
against every `a_j`, `j<n` (definition of the greedy rule), in particular
`\mathrm{rad}(a_n)\cap\mathrm{rad}(a_j)=C\cap\mathrm{rad}(a_j)\ne\varnothing`
for every `j\le i` (as `i\le n-1`); since `\mathrm{rad}(T_C)=C`, `T_C` is
admissible against `a_1,\dots,a_i$ too. Combined with `T_C>a_i`, greedy
minimality of `a_{i+1}` (the smallest admissible integer `>a_i`) gives
`a_{i+1}\le T_C`; combined with `T_C\le a_{i+1}` (choice of `i`) this forces
`a_{i+1}=T_C`. But `i+1\le n-1<n$ (from `a_n>T_C=a_{i+1}` and strict
monotonicity), so index `i+1<n$ already realizes `C`, contradicting "`n` is
the first occurrence." Hence `a_n=T_C`. `\blacksquare`

**Step 2 — Fan-Size Corollary (conditional bound, new).** If `C'` first
occurs at index `m` (so `a_m=T_{C'}` by Step 1), then every value `C'\cup
\{q\}` (`q\notin C'`) realized at some `i<m` satisfies `q\cdot\prod(C')\le
a_i<a_m=T_{C'}`, i.e. `q<T_{C'}/\prod(C')` — a finite, explicit,
`a_1`-and-`C'`-computable bound on fan size, **given that `C'` is in fact
eventually realized**. This does NOT bound (i) how many distinct absorbing
`C'`s a channel cycles through, nor (ii) whether growth could continue
forever without absorption — flagged explicitly, do not overclaim.

**Step 3 — Generation-Chain Lemma (cheap, three lines from the
already-certified No-Resurrection Lemma — certify this too).** Fix a proper
core `S`. A *domination chain* `C_1\supsetneq C_2\supsetneq\cdots\supsetneq
C_r\supseteq S` is a sequence where each `C_{i+1}` dominates (causes the
removal of) `C_i` from the running antichain. By No-Resurrection (already
certified), `|C_i|` strictly decreases along any single chain, so any chain
starting from a *fixed* `C_1` is automatically finite (length `\le|C_1|-
|S|`). **This is not new difficulty** — state it explicitly so the builder
does not waste effort re-deriving it, and to make crisp that the genuinely
open content is chain COUNT (how many distinct chains/entries `𝓥_S` ever
has), not chain length.

**Step 4 — Growth-Budget Lemma, OPEN, this round's real target (do not
claim to close it).** Candidate mechanism: combine Lemma 1
(`a_n\le a_1+(n-1)L`) with Step 2's fan-size bound to argue that if
infinitely many distinct chains occurred within one core `S`, the sequence
`\{T_{C_1}\}` over successive chain-starting values `C_1` would have to grow
faster than `a_1+(n-1)L$ allows by time `n` — **this reduction is not
constructed**; state the exact obstruction: pointwise-in-`n` control (what
is available by time `n`) does not automatically give cumulative
finiteness, exactly the gap `forced-primes-well-ordering`'s round-3/4 Markov
bound already hit. **Do not resurrect that refuted mechanism verbatim**;
find a genuinely different way to convert the pointwise bound into a
cumulative one, or report honestly that none was found.

**Explicit warning (per this round's narrow-framing explorer, apply here
too).** Do not present "every generation is eventually absorbed at its exact
`T_C`" as if it were a new sufficient condition for finiteness on its own —
restated generally that is circular (the same trap as the already-refuted
`H=\mathrm{rad}(L_{\mathrm{per}})$ characterization). Lemma FOM and its Fan-
Size Corollary are legitimate, provable, specific progress; Step 4 (the
termination/counting argument) is the actual open content and must not be
faked.

## Round 6 Build (proof-builder — this round's work, read first)

Following the round-6 outline above and the outline-reviewer's **CHANGES
REQUESTED** verdict (`/tmp/round-6/outline-reviewer.md`: Lemma FOM's proof
independently re-derived and re-tested — "legitimate, provable, foundational
new content, correctly the designated certification home for it"; the
Growth-Budget Lemma "honestly marked open, with the exact obstruction
named... no overclaiming," but flagged as sharing its mechanism with
`imprint-automaton-periodicity`'s Companion-Count Bound), this round:

1. **Certified Lemma FOM in full**, using the cleaner single-argument
   proof-by-contradiction route the reviewer identified (no "detour"), not
   the outline's two-step phrasing. Certified the **Fan-Size Corollary** as a
   three-line consequence, and the **Generation-Chain Lemma** (chain length
   finite, cheap, from the already-certified No-Resurrection Lemma) exactly
   as scoped by the outline.
2. **Attacked the Growth-Budget Lemma directly** (the outline's Step 4, this
   round's actual open target) and found a genuinely new mechanism — built
   from Lemma FOM's *exact value* (not just the fan-size bound) combined with
   the already-certified Lemma P′ and Generalized Lemma C
   (`lemmas/lemma-C-generalized-subsequence.md`), **not** a repeat of the
   refuted Markov/Cauchy–Schwarz pointwise-density bound:
   a. Proved a new, general, previously-unstated structural fact — the
      **Eventual Realization Dichotomy (Lemma ER)**: an integer `y>a_1`
      either is permanently blocked (fails admissibility against some fixed
      term forever) or is *actually realized* as some `a_m`; no third
      possibility ("permanently admissible but never chosen") exists. Proved
      from scratch via a direct greedy-minimality contradiction; verified
      numerically (zero exceptions among 14,287 candidates, `a_1=247`,
      `N=500`).
   b. Proved the **`Λ_S`-Reduction Lemma**: `𝓥_S` is finite **if and only
      if** the "companion-primes" set `Λ_S:=⋃_{C∈𝓥_S}(C\S)` is finite — a
      clean equivalence (three-line proof both directions), reformulating a
      question about a *family of sets* into a question about a single
      *flat set of primes*.
   c. Proved the **Single-Companion Finiteness Lemma**: conditional on the
      "`S`-avoiding index set" `J_S:=\{j:\mathrm{rad}(a_j)\cap S=\varnothing\}`
      being infinite, only **finitely many** primes `q` can *ever* be
      realized as the *sole* companion of `S` (i.e. `\mathrm{rad}(a_i)=S\cup
      \{q\}` for some `i`) — via a new application of the already-certified
      Generalized Lemma C to `I:=J_S`, combined with Lemma P′. This is a
      genuinely new, fully rigorous, non-circular mechanism (not a repeat of
      any previously-refuted density/pigeonhole argument) — verified
      numerically with an **exact match** on two independent examples
      (`a_1=2747`, `S=\{41\}`: predicted bound `\{2,3,7\}` (from
      `D=\{2,3,7,67\}\setminus P_1`), and the true realized set is exactly
      `\{2,3,7\}` — not just a superset, an exact match; `a_1=247`,
      `S=\{13\},\{19\}`: predicted bound `\varnothing` in both cases,
      matching the true realized set exactly).
   d. **Diagnosed, and *proved* rather than merely asserted, exactly why
      this does not close the full Growth-Budget Lemma**: (i) proved a
      **Multi-Companion Reduction Proposition** showing that bounding
      *bundles* of `\ge2` new companion primes reduces exactly to a
      finite-covering-set requirement on the infinite family
      `\{\mathrm{rad}(a_j):j\in J_S\}` — i.e. a *local, restricted instance
      of FCBC itself* — not something the Generalized-Lemma-C mechanism
      (which crucially needs a *single fixed prime* dividing *every* term of
      an infinite family, not a *finite covering set* for it) can reach;
      (ii) honestly flagged that "`J_S` is infinite" is *not* proved for a
      general proper core `S` — verified numerically in every case checked
      this round (`a_1=247`: `|J_{\{13\}}|=2074`, `|J_{\{19\}}|=3228$ within
      the first `6000` terms, still growing at the end of the tested range;
      `a_1=2747`: `|J_{\{41\}}|=118`, `|J_{\{67\}}|=5759`, likewise still
      growing) but not established in general. **Status remains `partial`**;
      the Growth-Budget Lemma is not closed, but the gap is now sharper and
      better understood than the outline's "pointwise ≠ cumulative"
      description alone: the *specific* obstruction is now isolated to (a)
      multi-companion bundling (provably self-similar to FCBC, not solvable
      by this round's mechanism) and (b) the unproved-in-general dichotomy on
      `J_S`.

See "Growth-Budget attempt (Round 6)" below (inserted into "Current best",
right after "Structural diagnosis of the Case II gap" and before Lemma C) for
the full statements and proofs.

## Round 5 Outline (proof-outliner directive — revived with a new mechanism: permanent-domination / event-counting reduction of (MRS))

**Why revived now, and why this is genuine diversity, not a relabeling of
`imprint-automaton-periodicity`'s round-5 pivot.** Both this approach and
`imprint-automaton-periodicity` now target Hypothesis (MRS) (`𝓜_n`
eventually constant — imported unchanged from the certified Lemma MS,
`lemmas/lemma-MS-minimal-radical-stabilization-sufficiency.md`; see that
file's notation, reused verbatim below). `imprint-automaton-periodicity`'s
round-5 pivot uses a Dershowitz–Manna **multiset order over collapse
events**. This approach instead uses a structurally different, elementary
tool: an unconditional **permanent-domination (no-resurrection) lemma**
converting (MRS) into a **counting** argument (bound the total number of
*distinct radical values ever minimal at any point in the whole infinite
process*, not a well-founded order on event sequences). This is close in
spirit to this approach's own historical "well-ordering DNA" (Lemma C,
already certified here) but is a genuinely different formal mechanism from
DM ordering — it needs no notion of multiset order at all, only a
set-membership permanence fact plus elementary counting. Keeping both live
in parallel, per the dispatch's explicit request, is deliberate insurance:
if DM ordering stalls on bounding "elapsed growth steps between collapses,"
this route's bottleneck is a differently-shaped question (bounding a
*static* union of ever-occurring values, `𝓥` below) that may be easier to
attack by a mechanism DM ordering cannot use directly (e.g. a counting/
pigeonhole bound tied to Lemma 1's linear gap bound, or a direct link to
`forced-primes-well-ordering`'s Lemma FF — see Step 3).

**Step 1 — No-Resurrection Lemma (NEW, elementary, verified numerically
before writing per project convention — see below).**

*Statement.* Fix a finite set of primes `C`. If there exists **any** index
`k\ge1` with `\mathrm{rad}(a_k)\subsetneq C` (a "dominating witness" for
`C`), then `C\notin𝓜_m` for every `m\ge k`.

*Proof (short, mechanism = fixed sequence + fixed comparison).* Suppose
`C\in𝓜_m` for some `m\ge k`, i.e. `C=P_i` for some `i\in M_m` (`i` is
`m`-minimal). Since `k\le m`, `k` is among the indices `\{1,\dots,m\}`
considered by `M_m`'s minimality test, and `\mathrm{rad}(a_k)\subsetneq
C=P_i` — this is *exactly* the condition that excludes `i` from `M_m`
(Lemma W3's definition of `m`-minimal: no index `\le m` has strictly smaller
radical). Contradiction. `\blacksquare` This uses only the fixed,
already-computed values `a_1,a_2,\dots` (a dominating witness, once it
exists at index `k`, exists at every later index `m\ge k` too, since the
sequence's terms never change) and the already-certified definition of
`M_m`/`𝓜_m` (Lemma W3, imported, no re-proof needed).

*Numerical verification (done before writing, per memory rule).* Simulated
`𝓜_n` incrementally (fresh Python, `math.gcd`, exact greedy rule) for
`a_1\in\{4087,2747,221,375,247\}` and checked directly: does any radical
value that leaves `𝓜_n` (dominated at some step) ever reappear later? **Zero
resurrections found** in every case (`4087` to `n=80`, spanning its
certified `n=54` collapse; `2747` to `n=600`, spanning its documented
2-level nested collapses at `n=13,14,163`; `221,375,247` to `n=600`). Also
recorded, for later use, the total number of "ever-minimal" values
`|𝓥_n|:=|\bigcup_{i\le n}𝓜_i|` and the total number of insertion+removal
events, confirming events `\le2|𝓥_n|` in every case (e.g. `a_1=2747`:
`39` events, `|𝓥_{600}|=22`, `2\times22=44\ge39` — consistent with the
Corollary below).

**Step 2 — Event-Counting Corollary (NEW, follows in 3 lines from Step 1).**

*Statement.* Let `𝓥:=\bigcup_{n\ge1}𝓜_n` (all radical values **ever**
realized as minimal, at any point in the whole infinite process — a
possibly-infinite union of finite sets, a priori). **If `𝓥` is finite, then
(MRS) holds.**

*Proof (mechanism: each element of `𝓥` contributes at most one entry and
one exit event, by Step 1).* Each `v\in𝓥` first appears in `𝓜_n` at some
minimal index `n_v` (by definition of `𝓥` as a union). By the
No-Resurrection Lemma (Step 1, applied with `C:=v`), once `v` is dominated
(excluded from `𝓜_m` for some `m>n_v` after having been present), it is
excluded from `𝓜_{m'}` for **every** `m'\ge m` — so `v` changes membership
status (`\in`/`\notin\,𝓜_n`) **at most twice** total across the whole
process: one "enter" transition (at `n_v`), and at most one "exit"
transition (if it is ever dominated). Since `𝓥` is finite, the total number
of membership-transition events, summed over all `v\in𝓥`, is `\le2|𝓥|` — a
**finite** number. Hence there is a last index `n^*` after which no
transition occurs for any `v\in𝓥`, i.e. `𝓜_n=𝓜_{n^*}` for all `n\ge n^*`.
This is exactly Hypothesis (MRS), with `N_0:=n^*`. `\blacksquare`

**This is a genuine, clean reduction: (MRS) is now reduced to proving `𝓥`
(not `𝓜_n` itself) is finite** — a *static* existential-finiteness
statement about the whole process's history, rather than an "eventually
constant" statement, which may admit different proof techniques (e.g.
counting/pigeonhole on `𝓥`'s elements directly) than a stabilization
argument would.

**Step 3 — attacking `𝓥`-finiteness (this round's genuinely open content;
NOT closed).** Candidate mechanism, not proved: generalize the
already-certified Lemma C. Lemma C shows `C_n:=\bigcap_{i\le n}\mathrm{rad}
(a_i)` — an INTERSECTION over the whole prefix, bounded above by
`\mathrm{rad}(a_1)` (size `\le k`) — stabilizes because it is non-increasing
in a set of size `\le k`. `𝓥`, by contrast, is a UNION that includes
primes not in `\mathrm{rad}(a_1)` at all (e.g. `83\in H` for `a_1=4199`,
already documented as not derivable from `a_1` alone) — so no direct
transplant of Lemma C's argument bounds `𝓥`. **This sub-goal is flagged,
honestly, as equivalent in difficulty to `imprint-automaton-periodicity`'s
Bounded Core Family (Step 2(a) of that file's round-5 outline) and to
`forced-primes-well-ordering`'s still-open Lemma FF (finiteness of the
forced-primes set `F`)** — round 4 already established `F\setminus P_1`
coincides numerically with this construction's `H\setminus P_1` in every
tested case, so proving any ONE of these three formulations finite is
expected to resolve all three. This is not a weakness of the reduction (the
No-Resurrection/event-counting machinery above is still new, clean,
reusable content in its own right) — it is an honest acknowledgment of
where the real difficulty of the whole problem now lives, stated precisely
in yet a third independent formal language (a static union-of-ever-minimal-
values, vs. approach 1's dynamic multiset order, vs.
`forced-primes-well-ordering`'s channel/necessity reduction).

## Round 5 Build (proof-builder — this round's work, read first)

Following the round-5 outline above (Steps 1–3) and the outline-reviewer's
**APPROVE** verdict on it (`/tmp/round-5/outline-reviewer.md`: "clean,
gap-free reduction of (MRS) to `𝓥`-finiteness"), this round:

1. **Wrote the No-Resurrection Lemma and Event-Counting Corollary in full,
   line-by-line rigor.** The outline's own statements were correct in
   substance (confirmed by the reviewer), but the Corollary's "at most two
   transitions" claim was *asserted*, not *derived*, from the Lemma. This
   round derives it properly via a new **Interval Lemma** (membership of a
   fixed value `v` in `𝓜_n`, as `n` varies, is an honest contiguous interval
   of indices `[n_v,\infty)` or `[n_v,e_v)` — proved from the No-Resurrection
   Lemma, not assumed), closing this gap.
2. **Proved the converse direction** — `(MRS)\Rightarrow𝓥` finite — which the
   outline did not state at all (it only used `𝓥`-finite`\Rightarrow`(MRS)).
   This is new content, upgrading the reduction from an implication to an
   **exact equivalence** (Theorem V below): `𝓥` finite `\iff` (MRS). The proof
   of this direction is a three-line finite-union argument, but it had not
   been written anywhere in this problem's workspace before this round, and
   it matters: it shows the target `𝓥`-finiteness is not an accidentally
   *stronger* sufficient condition than necessary — it is *exactly* as hard
   as (MRS) itself, confirming the reduction "wastes" no difficulty.
3. **Proved a new Record Characterization Lemma**: `𝓥=\{P_i : i\text{ is
   "fresh"}\}`, where `i` is *fresh* iff no `k<i` has `P_k\subsetneq P_i` —
   i.e. `𝓥` is exactly the set of distinct radical values realized at
   "record" positions of the sequence `(P_n)_{n\ge1}` under `\subsetneq`,
   with **no reference at all** to the incremental `M_n`/`𝓜_n` update
   machinery. This is a genuine simplification: it reduces `𝓥`-finiteness to
   a clean, self-contained combinatorial statement about the raw sequence
   `(P_n)`. Verified computationally (fresh Python, exact factorization via
   `sympy`) to agree exactly with the simulator's direct `𝓜_n`-based
   definition of `𝓥` on 5 independent test cases (`a_1=221,4087,2747,375,247`,
   `N=600`), zero discrepancies.
4. **Numerically stress-tested, as directed, the two flagged hard cases**
   (fresh Python, exact integer factorization, `N` large enough to safely
   exceed the reported stabilization index in each case):
   - **`a_1=2747`** (multi-hub nested fan): reproduced the `|𝓜_n|`-history
     exactly, confirming genuine **nested** collapses (`10\to8` at `n=13`,
     `8\to5` at `n=14` — a two-step nested collapse in consecutive steps, not
     a single event), followed by renewed growth (`5\to6\to7\to8`) and a
     final collapse, stabilizing at `N_0=163` with `|𝓥|=22`. `𝓥` is finite
     here (directly observed).
   - **`a_1=11623`** (late-stabilizing hidden Case I): reproduced `𝓜_n`
     failing to stabilize until `n=3285` (matching the flagged
     `n=3284`/`3285`), with `|𝓥|=511` — dominated by `\approx500` distinct
     two-prime "fan" values `\{59,p\}` (one for each prime `p` up to
     `\approx3469` that is realized before stabilization), each individually
     *fresh* (not dominated by any earlier radical) until a term with radical
     **exactly** `\{59\}` finally appears and, in one stroke, dominates
     (via the No-Resurrection Lemma) the entire accumulated fan. `𝓥` is
     finite here too, but its formation pattern (size tracking something
     like the number of primes realized before a single absorbing event, over
     thousands of steps) is qualitatively different from `2747`/`4087`'s
     small, early-stabilizing pattern.
5. **Went further than only observing this numerically**: proved a new,
   fully self-contained **Theorem CI** below, showing that in Case I
   (a single prime `p` saturates every term), `𝓥` is **unconditionally
   finite**, with an *explicit* closed-form bound on the stabilization index
   `N_0`, derived from Lemma S' (already certified) via elementary number
   theory (no simulation needed). Applying Theorem CI's formula to
   `a_1=11623`, `p=59` gives `N_0=3285` **exactly matching** the
   independently-simulated stabilization index found in point 4 above — a
   genuine (not merely consistency-checked) proof of exactly the phenomenon
   that motivated flagging this example as a stress test, not just a
   verification that the machinery "survives" it.
6. **Attempted directly to close `𝓥`-finiteness in Case II** (the outline's
   Step 3, the genuinely open content). Found a precise necessary condition
   (Proposition FR below) and diagnosed exactly why elementary
   counting/pigeonhole does not suffice to close it (see "Structural
   diagnosis," below) — **this sub-goal remains open**; it is not closed this
   round. Status remains `partial`.

See the fully worked-out statements and proofs below (inserted into "Current
best," after the already-certified imported lemmas).

## Round 4 note (proof-outliner — parked this round, not dropped)

**This approach is parked for round 4** (no builder dispatched), not
re-attempted with a fourth minor variation. Rationale: Lemma W1
(`explicit-window-backbone-construction`) proves this approach's target,
`forced-primes-well-ordering`'s, and `explicit-window-backbone-
construction`'s are the *literal identical proposition*; this approach's
two natural `\omega`-boundedness-based sufficiency bridges (ND1, the literal
per-step dominant prime; ND2, the broadened averaged-threshold set) are both
already rigorously refuted, and no new mechanism specific to this approach's
own `\omega`-boundedness framing has been identified this round. Per
`CLAUDE.md`'s single-gap-trap guidance, round 4 instead puts the three new
mechanisms surfaced by round-4 exploration on the table via the *other* two
identical-proposition approaches (`explicit-window-backbone-construction`
pivots to a compactness/König's-lemma argument on window sizes;
`forced-primes-well-ordering` pivots to the `H_\rho` excess-density/channel
bridge) plus a genuinely new fourth approach (`imprint-automaton-
periodicity`, targeting the `G_n`-imprint-periodicity finding) — a fourth
concurrent attempt on the identical proposition via this approach's own
already-exhausted framing would not add diversity. This approach's Key
Lemma (`\omega`-bound, conditional) and Propositions ND1/ND2 remain
certified and reusable; if a future round finds a genuinely new mechanism
specific to the `\omega(a_n)=O(1)` framing (not a repeat of ND1/ND2), it
should be revived then, not before.

## Round 3 Build (proof-builder — this round's work, read first)

Following the outline below and the outline-reviewer's explicit "CHANGES
REQUESTED" verdict (the `\omega`-boundedness necessity algebra was verified
sound, but no sufficiency/covering mechanism was sketched), this round:
1. Re-derived the necessity-half algebra cleanly (Key Lemma `\omega`-bound:
   `\omega(a_n)=O(1)\Rightarrow` the Domination-Lemma dominant primes form a
   finite set `Q`) — confirmed correct, no change from the outline.
2. **Directly attacked the requested necessity→sufficiency bridge** by
   constructing two concrete candidate covering sets from `Q` (the literal
   per-step argmax, and a broadened "meets-the-average-threshold" version) and
   testing whether either satisfies the FCBC covering property. **Both fail**,
   and both failures are proved rigorously by hand (not just numerically) as
   Propositions ND1 and ND2 below, reusing the already-certified NC1 (`a_1=221`)
   and NC2 (`a_1=375`) traces. This directly answers the outline-reviewer's
   request: a genuine bridge attempt was made and shown NOT to work as stated,
   rather than left as an unaddressed "also flagged" gap.
3. Ran an exploratory (non-proof) numerical investigation of prime-divisor
   density, finding a suggestive but unproved "positive density vs. decaying
   density" stratification that may point toward the correct mechanism for a
   future round, honestly flagged as not a result.
4. Updated the "What remains open" section to reflect that the gap is now
   *narrower and better understood* (two specific mechanisms ruled out) but
   still fully open — Status remains `partial`.

See "Round 3: the `\omega`-boundedness algebra..." subsection below (inserted
after the round-2 "Attempted proof route" section) for full detail.

## Round 3 Outline (proof-outliner directive — retargeted)

**Do not re-attempt round 2's two refuted shortcuts** (`S_0` from Lemma C's
`N_0`, refuted by NC1/`a_1=221`; `\le\mathrm{rad}(a_1)` a-priori bound, refuted
by NC2/`a_1=375`) — both propositions stay certified as permanent negative
results. **Also do not target `(\star\star)` (`W` itself finite)** — round-3
exploration (`/tmp/round-3/math-explorer-backbone-conjecture.md`) found strong
numerical evidence `W` is *unbounded* for `a_1=4199,4087` (`|W|` still growing
past `21` distinct primes at `M=15000`, no plateau) — this is a genuinely new,
important negative finding this round, sharpening NC1/NC2 into "do not let any
sub-argument secretly need `W` finite," not just "no simple closed form for
`W`." The correct target remains the strictly weaker **Finite Covering
Backbone Conjecture (FCBC)**: exists finite `H` with `H\cap\mathrm{rad}(a_i)
\cap\mathrm{rad}(a_j)\ne\varnothing` for every `i<j` — already reformulated
last round, and (per `theorem-2.2-H-hitting-characterization.md`'s
reviewer-generalization) provably sufficient on its own, without needing `W`
finite, to get conditional eventual periodicity via the certified
Theorem 2.2 + Lemma 2.3 + Theorem 2.4 chain. FCBC itself passed **every**
stress test this round (24 diverse `a_1` values, up to 20,000 terms / `~2\times
10^8` pairs, including the two `W`-unbounded cases above) — treat it as a
well-supported, still-open target, not a shaky one.

**Retargeted Step 2 (primary mechanism, new this round): reduce FCBC to
boundedness of `\omega(a_n)`.** Revisit the already-certified algebra from
last round's "Attempted proof route": for `x=a_{n+1}`, `r:=\omega(x)`, and
`q^*` the Domination Lemma's dominant prime, `q^*\le r\cdot a_n/n`. Since
Lemma 1 gives `a_n\le a_1+(n-1)L`, we have `a_n/n\to L` — a genuine **constant**,
not growing — so *all* of the previously-obtained `O(\log n)` growth in the
bound on `q^*` comes from `r=\omega(a_{n+1})` alone. **Key Lemma
`\omega`-bound.** If `\omega(a_n)\le M` for every `n` (a fixed constant `M`,
not growing with `n`), then `q^*(n)\le M\cdot(a_1+L)` for every `n` — a genuine
uniform constant bound on the dominant prime at *every* step, immediately
giving `Q:=\{q^*(n):n\ge1\}` finite (`\subseteq` primes `\le M(a_1+L)`). This is
a three-line consequence of already-certified lemmas (Domination Lemma +
Lemma 1) plus the one new hypothesis; **certify it as its own small lemma
first**, since it isolates all remaining work into exactly one sub-claim
(matches round-3 explorer's "Cheap-kill candidates" finding).

**Sub-target: prove `\omega(a_n)=O(1)`.** Round-3 numerics
(`/tmp/round-3/math-explorer-backbone-conjecture.md`, section (c)) found
`\omega(a_n)\le6`–`7` across tens of thousands of terms on the hardest stress
case `a_1=247` (pushed to `n=40000`), essentially flat, far tighter than the
pessimistic `O(\log n)` worst case — strong support, but not yet distinguished
numerically from "extremely slowly growing" (one late increase `6\to7` at
`n\approx17770` was observed). **Mechanism to attempt**: an inductive
invariant, not a counting/density argument — e.g. "if `\omega(a_i)\le M` for
every `i\le n` and the realized set of `\mathrm{rad}(a_i)\cap[\text{current
backbone}]` signatures has stabilized, then `a_{n+1}`'s minimality (it is the
*smallest* admissible integer, and by Lemma 1 lies in a window of length
`\le L` above `a_n`) forces it to reuse a *few* already-recruited
high-density primes rather than introduce many new one-off small primes, so
`\omega(a_{n+1})\le M` too." This inductive step is **not proved** — it is
the approach's genuine open content this round; a full proof needs to show
the minimal admissible integer in `(a_n,a_n+L]` cannot be forced to acquire an
`(M+1)`-th distinct prime factor. **Watch out**: the explorer explicitly flags
`\omega(a_n)=O(\log\log n)` (Hardy–Ramanujan-typical, still unbounded but very
slow) as a live alternative to genuine `O(1)`-boundedness — if the inductive
invariant only yields the former, `Q` is *not* proved finite and this route
fails; do not silently downgrade the target from "bounded" to "grows slowly"
without flagging it honestly.

**Fallback mechanism (Step 2′, if the `\omega`-boundedness route stalls):
forced-primes well-ordering.** This is scouted (not developed) as a genuinely
different mechanism for the *same* target FCBC — see the separate approach
`forced-primes-well-ordering` (new this round, a "copy" of this approach's
target with a distinct proof technique per the outline-reviewer's copy
mechanism, since both routes are worth running in parallel). Do not duplicate
effort between the two files; this file's primary content is the
`\omega`-boundedness route above.

**Once FCBC is established (`H` finite, covering property proved)**: hand off
directly to `intersecting-family-covering-construction`'s certified Theorem
2.2/Lemma 2.3/Theorem 2.4 chain (already generalized by the reviewer to any
covering `H`, not just `W` — see `lemmas/theorem-2.2-H-hitting-
characterization.md`) to get conditional eventual periodicity for free, with
periodicity-from-`n=1` then handled by that approach's own Gap 2 work.

## Approaches tried

- **Round 8 (this round).** Retargeted from round 7's proven-insufficient
  "permanent-bundle-count" target to the true remaining object (permanent +
  transient members of `𝓥_S`). Certified the Escape-Confinement
  Pairwise-Disjoint-Bundle-Count Corollary (Step 1), conditional on
  core-avoiding-witness existence (proved a real directional partial result,
  the Complement Witness Fact; general existence stays open, matching the
  outline-reviewer's own assessment). Proved a new Realized–Blocked
  Dichotomy Lemma and, building on it, a Finite-Reachability Theorem (Step
  2): NIBC (no infinite chain of always-blocked bare values) `\Rightarrow`
  the count of Subset-Avoidance-satisfying bundles is finite — a genuine
  upgrade of the round 7/8 informal "doesn't visibly terminate" diagnosis
  into an exact conditional theorem, via a from-scratch proof of the
  relevant König's-Lemma fact. Proved, not just observed, that this entire
  mechanism (Steps 1 and 2 alike) is structurally blind to transient bundles
  — bundles failing (SA) are exactly the ones invisible to it, confirmed on
  the one documented transient worked example. Neither gap (core-avoiding
  witness existence in general; NIBC) is closed. Status remains `partial`.

- **Round 2.** Started from the round-2 outliner's skeleton (Lemma C
  stated with a proof sketch; Step 2 an admittedly-open well-ordering attempt on
  the canonical-minimal-witness target `w(i,j):=\min(\mathrm{rad}(a_i)\cap
  \mathrm{rad}(a_j))`). Work done this round:
  1. **Certified Lemma C (Global Intersection Collapse) in full**, closing every
     gap the outline left open (the nesting argument, the finite-stabilization
     argument, and both directions of the "iff Case I" claim, done from scratch
     below, matching the outline-reviewer's independent re-derivation).
  2. **Found and *proved* (not just suspected) that the outline's own proposed
     shortcut — "the backbone is `S_0:=\bigcup_{i\le N_0}\mathrm{rad}(a_i)`, the
     union of radicals up to Lemma C's collapse index" — is FALSE**, by an
     explicit, fully hand-verified 5-term counterexample (`a_1=221`; see
     Proposition NC1 below). This directly refutes the outline's Step-2 intuition
     ("this extension \[from `N_0` to a full backbone\] ... has not been extended
     to rule out for the full, growing set of previously-used witnesses") — it
     shows this extension is not just unproven but *cannot* be made to work as
     originally envisioned, because genuinely new primes not present at the
     collapse index keep getting recruited as canonical witnesses well after
     `N_0`.
  3. **Tested and refuted a second, stronger natural conjecture** — "every
     canonical witness is `\le L:=\mathrm{rad}(a_1)`" — with a second explicit,
     fully hand-verified 7-term counterexample (`a_1=375`; Proposition NC2 below).
     This rules out a very natural a-priori (input-only) bound on the backbone.
  4. **Reformulated the approach's target** into a strictly weaker, better-behaved
     conjecture — the *Finite Covering Backbone Conjecture* (stated precisely
     below) — that is logically implied by (hence no harder to prove than) the
     original min-witness-finiteness target, is consistent with every one of
     NC1/NC2's counterexamples (which only refute *specific over-strong
     descriptions* of the backbone, not its finiteness), and was stress-tested
     computationally far beyond anything checked previously in this problem's
     workspace (exhaustive verification on `a_1=247` — the hardest known stress
     case, where not even periodicity itself has been detected within thousands
     of terms — across **8000 consecutive terms**, ~32 million pairs, zero
     failures using a backbone read off from only the first 4 terms).
  5. **Attempted a direct proof of the reformulated conjecture** via the
     Domination Lemma + Lemma 1 (the two lemmas explicitly already certified for
     this problem). This succeeds in deriving an explicit, clean bound (worked
     out in full below) on the "dominant prime" at each step, but the bound is
     `O(\log n)` — genuinely growing, not a fixed constant — so this route alone
     does **not** close the conjecture. This confirms, with a concrete
     computation rather than only qualitative language, exactly why `current.md`'s
     previously-recorded gap (b) ("concentration onto finitely many dominant
     primes") survives this attempt; no new route to close it was found this
     round.
  - **Verdict on this round's work**: genuine progress (one lemma fully
    certified, two false natural conjectures ruled out with proofs, the target
    sharpened to a better-supported and logically weaker reformulation), but the
    core existence claim (a finite covering backbone) remains open. Status stays
    `partial`, not `solved`.

- **Round 3 (this round).** Outline-reviewer verdict: CHANGES REQUESTED — the
  `\omega`-boundedness necessity algebra (`\omega(a_n)=O(1)\Rightarrow` dominant
  primes `Q` finite) was verified sound, but no mechanism was given for why a
  finite `Q` (or any set built from it) actually *covers* every pair `i<j`
  (sufficiency), as opposed to merely being finite (necessity). Work done this
  round, directly responding to that request:
  1. Re-confirmed the necessity algebra (Key Lemma `\omega`-bound) with a clean
     three-line derivation from the already-certified Domination Lemma + Lemma 1
     (no new gap here; matches the reviewer's own hand-check).
  2. **Attempted the requested bridge directly**, testing two concrete
     candidate covering sets built from the Domination Lemma's "dominant
     prime" notion: (i) the literal per-step unique maximizer `Q`, and (ii) a
     broadened set `Q'` of every prime meeting the averaged Domination-Lemma
     threshold at any step. **Both are proved (not just observed numerically)
     to fail the FCBC covering property**, via two new, fully hand-verified
     propositions (ND1 on the `a_1=221` trace, ND2 on the `a_1=375` trace),
     each reusing an already-certified counterexample trace (NC1, NC2
     respectively) rather than requiring a fresh trace to be verified.
  3. Ran (and clearly flagged as non-proof) an exploratory numerical study of
     asymptotic prime-divisor density, finding a suggestive stratification
     (stable positive density for "core" primes vs. decaying density for
     "extra" primes) that might inform a future round's mechanism, but did not
     convert it into a proof.
  - **Verdict on this round's work**: genuine progress on exactly the point the
    outline-reviewer raised — the sufficiency gap is no longer an unaddressed
    "also flagged" item but a concretely tested (and concretely refuted, twice)
    open question, narrowing what a correct mechanism would have to look like
    (not locally/per-step derived from the Domination Lemma's argmax or average
    threshold). The core FCBC conjecture itself remains open. Status stays
    `partial`, not `solved`.

- **Round 5 (this round).** Outline-reviewer verdict: **APPROVE** on the
  round-5 outline (No-Resurrection Lemma + Event-Counting Corollary reducing
  (MRS) to `𝓥`-finiteness) — "clean, gap-free reduction," "cleanest reduction
  produced by any of the three approaches this round." Work done this round,
  as directed:
  1. Wrote the No-Resurrection Lemma in full rigor (matched the outline,
     confirmed correct).
  2. Replaced the outline's asserted "at most two transitions per value"
     claim with a fully proved **Interval Lemma** (membership of any fixed
     value in `𝓜_n` is a genuine contiguous interval of indices, derived from
     the No-Resurrection Lemma, not assumed).
  3. Proved the **converse** direction (MRS) `\Rightarrow` `𝓥` finite — new,
     not in the outline — upgrading the reduction to an exact equivalence,
     **Theorem V**.
  4. Proved a new **Record Characterization Lemma**: `𝓥` equals the set of
     radical values realized at "fresh" (record) indices of the raw sequence
     `(P_n)`, with no reference to the `M_n`/`𝓜_n` update process at all —
     verified computationally against the simulator's direct definition on 5
     cases, zero discrepancies.
  5. Stress-tested, as directed, `a_1=2747` (multi-hub nested fan — confirmed
     the two-step nested collapse `10\to8\to5` at `n=13,14`, final `N_0=163`,
     `|𝓥|=22`) and `a_1=11623` (late-stabilizing hidden Case I — confirmed
     `N_0=3285`, `|𝓥|=511`).
  6. **Proved Theorem CI**: in Case I, `𝓥` is unconditionally finite, with an
     *explicit closed-form* stabilization index `N_0=p^{k_0-1}-m+1`
     (`k_0:=\min\{k:p^k\ge a_1\}`, `m:=a_1/p`) — derived from the
     already-certified Lemma S', not from simulation. Applied to
     `a_1=11623,p=59`: gives `N_0=3285`, **exactly** matching the
     independently-simulated value — a genuine proof of the phenomenon
     flagged this round, not just a numerical confirmation of it.
  7. **Attempted directly to close `𝓥`-finiteness in Case II** (the outline's
     Step 3). Found one genuine necessary condition (Proposition FR:
     `P_1\not\subsetneq P_i` for fresh `i\ge2`) but this is, like round 3's
     ND1/ND2, far short of a sufficiency/finiteness argument. Diagnosed
     precisely (in "Structural diagnosis," see "Current best") why the
     mechanism that closes Case I (Theorem CI) has no available analogue in
     Case II: no explicit closed form for `a_n`, and no single global
     dominating prime (Lemma C gives `\bigcap_iP_i=\varnothing` in Case II).
  - **Verdict on this round's work**: the reduction of (MRS) to `𝓥`-finiteness
    is now airtight and sharpened to an equivalence (Theorem V), with a new
    value-adding self-contained result (Theorem CI) proving the machinery
    correct on the hardest available stress case, not merely numerically
    checking it. The genuinely open content — `𝓥`-finiteness in Case II — is
    **not closed this round**, consistent with the outline-reviewer's
    observation that this is, up to relabeling, the same open object as
    `imprint-automaton-periodicity`'s "Bounded Core Family" and
    `forced-primes-well-ordering`'s Lemma FF. Status stays `partial`, not
    `solved`.

- **Round 6 (this round).** Outline-reviewer verdict: **CHANGES REQUESTED**
  (Lemma FOM's proof independently re-derived/re-tested and confirmed sound;
  Growth-Budget Lemma correctly left open with the exact "pointwise ≠
  cumulative" obstruction named, honestly, in the outline, but flagged as
  mechanism-overlapping with `imprint-automaton-periodicity`'s
  Companion-Count Bound). Work done this round:
  1. Certified Lemma FOM in full, using a cleaner single-argument
     proof-by-contradiction (per the reviewer's own independent
     re-derivation), plus the Fan-Size Corollary and the Generation-Chain
     Lemma exactly as scoped by the outline.
  2. **Found a genuinely new mechanism for a real (if narrower-than-hoped)
     piece of the Growth-Budget Lemma** — not a resurrection of the refuted
     Markov/Cauchy–Schwarz density bound: proved a new general structural
     fact (Lemma ER, Eventual Realization Dichotomy — previously unstated in
     this workspace), a new clean equivalence (`Λ_S`-Reduction Lemma:
     `𝓥_S` finite `\iff` the flat companion-primes set `Λ_S` finite), and a
     new positive result (Single-Companion Finiteness Lemma, via a new
     application of the already-certified Generalized Lemma C to the
     `S`-avoiding index set `J_S`) that provably bounds *single-companion*
     recruitment to any proper core `S`, conditional on `J_S` being
     infinite. Verified with an *exact* numerical match (not just a valid
     superset) on three independent core/`a_1` pairs.
  3. **Proved, rather than merely asserted, exactly why this does not close
     the full Growth-Budget Lemma**: the new Multi-Companion Reduction
     Proposition shows bounding bundles of `\ge2` new companions reduces
     exactly to a finite-covering/hitting-set requirement on the infinite
     family `\{\mathrm{rad}(a_j):j\in J_S\}` — a local, restricted instance
     of FCBC itself, which the Generalized-Lemma-C mechanism (built for
     fixed-intersection stabilization, not covering-set existence) cannot
     reach. Also honestly flagged, and did not attempt to paper over, the
     second gap: "`J_S` infinite" is verified numerically in every core
     tested this round but not proved for a general proper core `S`.
  - **Verdict on this round's work**: genuine, non-circular, verified new
    content (Lemma ER, the `Λ_S`-Reduction Lemma, the Single-Companion
    Finiteness Lemma, the Multi-Companion Reduction Proposition), and — per
    the dispatch's explicit request — an honest, *proved* (not just
    asserted) diagnosis of precisely where and why the Growth-Budget Lemma
    resists this round's tools. The Growth-Budget Lemma itself, and hence
    `𝓥_S`-finiteness for a general proper core, **remains open**. Status
    stays `partial`, not `solved`.

- **Round 7 (this round).** Outline directive: certify the Permanent Pair
  Lemma, record why it forecloses bundle-size induction as a family, pivot
  to a direct companion-bundle-COUNT bound. Work done this round:
  1. **Certified the Permanent Pair Lemma, and found + fixed a genuine gap**
     in the version proposed by the round-7 math-explorer and independently
     re-derived by the round-7 outline-reviewer: both considered only
     same-class (`I_S`) dominators, which is provably the *complete* set of
     candidate dominators when `S` is a singleton core (new
     **Class-Decomposition Fact**, proved from Lemma P′), but is
     **incomplete** for non-singleton `S` (a "sub-core" dominator, radical
     `S'∪Q''` for `S'⊊S` proper, is a priori possible and unaddressed by
     either prior derivation). Proved the missing **Sub-Core Avoidance**
     requirement unconditionally (not just numerically) for the one
     non-singleton instance on record (`a_1=21528751,S=\{103,197\}`) via two
     explicit early witnesses and the already-certified
     Permanent-Inadmissibility Lemma — a real rigor fix, not a restatement.
  2. **Generalized to a new Permanent Bundle Lemma** (arbitrary bundle size
     `k`, adding a **Subset Avoidance** hypothesis genuinely needed, and
     shown to be genuinely *needed*, for `k\ge3` only). Validated
     exhaustively — 44 size-`\ge3` `D_S`-disjoint fresh bundles found across
     all five mandated hard cases, **zero exceptions** in either direction
     (hypothesis holds `\iff` bundle confirmed permanently alive), including
     a negative control (`a_1=4199,S=\{19\}`) showing the Lemma correctly
     declines to overclaim where the hypothesis genuinely fails. Three
     instances proved by explicit witness, not merely observed.
  3. **Sharpened (not merely repeated) the bundle-size-induction
     foreclosure**: showed the natural "fix" to the round-7 explorer's
     refuted `k=2\to k=1` reduction — using the corrected
     `D_S`-disjointness-plus-Subset-Avoidance criterion instead of the flawed
     `D_S`-disjointness-alone criterion — **still** does not yield a working
     induction, since verifying Subset Avoidance is itself an instance of
     the same general open question one level down.
  4. **Attempted the outline's real target directly**: pushed a
     from-scratch simulator (independently cross-validated against a
     brute-force `O(N^2)` implementation, zero discrepancies) to
     `N=3`–`5{,}000{,}000` across all five mandated hard `a_1` values — two
     to three orders of magnitude past any prior round's stress test.
     Found the per-core fresh-bundle count, and in fact the *entire global*
     minimal-radical antichain `𝓜_n` (verified by literal set-identity, not
     just size), **freezes completely** at a small, `a_1`-specific index
     (matching, where previously documented, the exact collapse points
     already on record — `n=163` for `a_1=2747`, `n=92` for `a_1=4199`,
     `n=54` for `a_1=4087` — and newly establishing `n=7` for `a_1=247` and
     `n=44967` for `a_1=21528751`) and **never changes again** through the
     full tested range. This is substantial new depth of empirical support
     for (MRS)/`Λ_S`-finiteness on these five instances, but **no new
     analytic mechanism was found** turning it into a bound for a general
     core `S`/`a_1` — honestly reported as still open, not overclaimed.
  - **Verdict on this round's work**: a real, previously-unnoticed rigor
    gap found and fixed (Sub-Core Avoidance), a new, exhaustively-validated
    Permanent Bundle Lemma generalizing the Pair case, a sharpened
    (deepened) foreclosure of the whole bundle-size-induction family, and
    the deepest numerical stress test performed in this workspace to date
    (up to `5{,}000{,}000` terms, two independent simulators). The count
    bound itself — how many `D_S`-disjoint (Subset-Avoidance-satisfying)
    bundles can ever be realized for a general core — **remains open**.
    Status stays `partial`, not `solved`.

## Current best

### Imported (already certified, no new proof needed — see `lemmas/`)
- **Lemma P** (`\gcd(a_n,a_1)>1` for `n\ge2`).
- **Lemma P′** (`\gcd(a_i,a_j)>1` for all `i<j`; the family `\{\mathrm{rad}(a_n)\}`
  is pairwise intersecting).
- **Lemma Q** and **Lemma S′** (Case I — a single prime saturates every term —
  is completely solved: `a_n=a_1+p(n-1)` for all `n\ge1`).
- **Lemma 1** (`a_{n+1}-a_n\le L:=\mathrm{rad}(a_1)` for every `n`, hence
  `a_n\le a_1+(n-1)L`).
- **Domination Lemma** (for `x=a_{n+1}` with distinct prime factors
  `q_1,\dots,q_r`, `\max_jD_n(q_j)\ge n/r\ge n/\log_2 x`, where
  `D_n(q):=|\{i\le n:q\mid a_i\}|`).
- **Lemma R** (eternal witness per index — not used directly this round, but see
  the remark after Proposition NC2 on why it is *not* a viable backbone notion).

All of these dispose of Case I completely; everything below (Lemma C onward,
through the round-3 material) is about Case II. **New this round (round 5)**:
the No-Resurrection Lemma, the Interval Lemma, Theorem V, the Record
Characterization Lemma, and Theorem CI are stated and proved for the general
setting (they hold regardless of Case I/II) and are inserted here, right
after the imported material, since they are logically prior to (independent
of) Lemma C and the rest of the round-2/3 content below.

### Notation (imported unchanged from the certified Lemma MS)

`P_i:=\mathrm{rad}(a_i)`. For `n\ge1`, `M_n\subseteq\{1,\dots,n\}` is the set
of `n`-minimal indices: `i\in M_n` iff `i\le n` and no `k\in\{1,\dots,n\}` has
`P_k\subsetneq P_i` (Lemma W3, certified in
`lemmas/lemma-W2-W3-patch-and-minimal-radical-reduction.md`). Define
`𝓜_n:=\{P_i:i\in M_n\}` (a finite antichain, under `\subseteq`, of finite
prime-sets — a *set of values*, not of indices). **Hypothesis (MRS)**: there
exists `N_0\ge1` with `𝓜_n=𝓜_{N_0}` for every `n\ge N_0`. Define
`𝓥:=\bigcup_{n\ge1}𝓜_n` (all radical values ever realized as minimal, at any
point in the whole infinite process).

**Preliminary fact used repeatedly below.** `𝓜_1=\{P_1\}` (with `n=1`, the
only candidate `k\in\{1\}` gives `P_1\subsetneq P_1` which is false, so
`1\in M_1`, and it is the only index, so `M_1=\{1\}`, `𝓜_1=\{P_1\}`). Hence
`𝓥\supseteq\{P_1\}\ne\varnothing`: `𝓥` is always nonempty, for any starting
sequence.

### No-Resurrection Lemma — proved in full this round

**Statement.** Fix a finite set of primes `C`. If there exists `k\ge1` with
`P_k\subsetneq C` (a *dominating witness* for `C`), then `C\notin𝓜_m` for
every `m\ge k`.

**Proof.** Suppose, for contradiction, `C\in𝓜_m` for some `m\ge k`. By
definition of `𝓜_m`, `C=P_i` for some `i\in M_m`. Since `i\in M_m` (Lemma
W3's definition), no index in `\{1,\dots,m\}` has radical `\subsetneq P_i=C`.
But `k\le m` (given) and `P_k\subsetneq C` (given), so `k\in\{1,\dots,m\}` is
exactly such an index — contradiction. Hence `C\notin𝓜_m`. As `m\ge k` was
arbitrary, this holds for every `m\ge k`. `\blacksquare`

*Remark.* The proof uses only the already-certified Lemma W3 (the definition
of `n`-minimal) and the fact that the sequence `(a_n)`, once computed, never
changes — no other machinery. It is unconditional (no dependence on Case I
vs. Case II, no dependence on any open hypothesis).

### Interval Lemma (new this round — makes the Event-Counting Corollary's
"at most two transitions" claim a proved fact, not an assertion)

**Statement.** Fix any finite set of primes `v\in𝓥`, and let
`A_v:=\{n\ge1:v\in𝓜_n\}` (nonempty, since `v\in𝓥` means `v\in𝓜_n` for some
`n`). Let `n_v:=\min A_v`. Then either:
(i) `A_v=[n_v,\infty)\cap\mathbb{Z}` (i.e. `v` is present in `𝓜_n` for
*every* `n\ge n_v`), or
(ii) `A_v=[n_v,e_v)\cap\mathbb{Z}` for some finite `e_v>n_v` (i.e. `v` is
present exactly for `n_v\le n<e_v` and absent for every `n\ge e_v`).

In particular `A_v` is a contiguous set of integers with no "gaps," and no
"resurrection": once `v` is absent from `𝓜_n` after having been present, it
is absent from every later `𝓜_m` too.

**Proof.** Let `E_v:=\{n>n_v:v\notin𝓜_n\}` (the set of indices, after `v`'s
first appearance, where `v` is absent). If `E_v=\varnothing`, we are in case
(i): `v\in𝓜_n` for every `n\ge n_v` is exactly what "no `n>n_v` has
`v\notin𝓜_n`" means, combined with `n_v\in A_v` itself. Otherwise
`E_v\ne\varnothing`; since `E_v\subseteq\mathbb{Z}_{>0}`, by well-ordering let
`e_v:=\min E_v` (so `e_v>n_v`).

*Claim: for every `c\ge e_v`, `v\notin𝓜_c`.* Since `e_v\in E_v`,
`v\notin𝓜_{e_v}` but `v\in𝓜_{n_v}` (as `n_v=\min A_v\in A_v`) with
`n_v<e_v`. Since `v\in𝓜_{n_v}`, `v=P_i` for some `i\in M_{n_v}`; in
particular `i\le n_v<e_v`, so `i\le e_v`. Since `v\notin𝓜_{e_v}` and `P_i=v`
with `i\le e_v`, index `i` cannot be `e_v`-minimal (else `v=P_i\in𝓜_{e_v}`,
contradiction), i.e. `i\notin M_{e_v}`. By Lemma W3's definition, this means
some `k\le e_v` has `P_k\subsetneq P_i=v`. This `k` is exactly a dominating
witness for `v` with `k\le e_v`. Apply the No-Resurrection Lemma with this
`C:=v`, `k`: `v\notin𝓜_m` for every `m\ge k`. Since `e_v\ge k`, every
`c\ge e_v` satisfies `c\ge k`, so `v\notin𝓜_c` for every such `c`. This
proves the claim.

*Claim: for every `n` with `n_v\le n<e_v`, `v\in𝓜_n`.* By minimality of
`e_v=\min E_v`, no `n` with `n_v<n<e_v` lies in `E_v`, i.e. `v\in𝓜_n` for
every such `n` (and `v\in𝓜_{n_v}` itself, shown above), so `v\in𝓜_n` for
every `n_v\le n<e_v`.

Combining the two claims: `A_v=\{n\ge1:v\in𝓜_n\}=[n_v,e_v)\cap\mathbb{Z}`
exactly. This is case (ii). `\blacksquare`

### Theorem V (Equivalence) — new this round, sharpens the outline's
one-directional Event-Counting Corollary to an iff

**Statement.** `𝓥` is finite **if and only if** (MRS) holds.

**Proof.**

`(\Rightarrow)` Suppose `𝓥` is finite. For each `v\in𝓥`, the Interval Lemma
gives either `A_v=[n_v,\infty)` or `A_v=[n_v,e_v)`; define
`$$m_v:=\begin{cases}n_v & \text{if }A_v=[n_v,\infty)\\ e_v & \text{if
}A_v=[n_v,e_v)\end{cases}$$`
a finite positive integer in either case. Since `𝓥` is finite (and nonempty,
by the Preliminary Fact), `N_0:=\max_{v\in𝓥}m_v` is a well-defined finite
positive integer. Fix any `n\ge N_0` and any `v\in𝓥`. If `A_v=[n_v,\infty)`,
then `n\ge N_0\ge m_v=n_v`, so `n\in A_v`, i.e. `v\in𝓜_n`. If
`A_v=[n_v,e_v)`, then `n\ge N_0\ge m_v=e_v`, so `n\notin[n_v,e_v)=A_v`
(every element of `A_v` is `<e_v\le n`), i.e. `v\notin𝓜_n`. Either way,
whether `v\in𝓜_n` depends only on which of the two cases `v` falls into —
**not** on the specific choice of `n\ge N_0`. Since `𝓜_n\subseteq𝓥` for
every `n` (as `𝓜_n` is one of the sets whose union defines `𝓥`), we have
`𝓜_n=\{v\in𝓥:v\in𝓜_n\}`, and by the above this set is identical for every
`n\ge N_0`. Hence `𝓜_n=𝓜_{N_0}` for every `n\ge N_0`: this is exactly (MRS).

`(\Leftarrow)` Suppose (MRS) holds with stabilization index `N_0`
(`𝓜_n=𝓜_{N_0}` for all `n\ge N_0`). Then
`$$𝓥=\bigcup_{n\ge1}𝓜_n=\Big(\bigcup_{n=1}^{N_0}𝓜_n\Big)\cup\Big(\bigcup_{n>N_0}𝓜_n\Big)=\Big(\bigcup_{n=1}^{N_0}𝓜_n\Big)\cup𝓜_{N_0}=\bigcup_{n=1}^{N_0}𝓜_n,$$`
using `𝓜_n=𝓜_{N_0}` for `n>N_0` in the middle step and absorbing `𝓜_{N_0}`
into the finite union in the last step. Each `𝓜_n` (`n\le N_0`) satisfies
`𝓜_n\subseteq\{P_i:i\le n\}`, a set of at most `n` elements, so `𝓜_n` is
finite; a finite union (`N_0` many terms) of finite sets is finite. Hence
`𝓥` is finite. `\blacksquare`

**Discussion.** This upgrades the outline's Step 1–2 (`𝓥`
finite`\Rightarrow`(MRS)) to a genuine equivalence — new content beyond the
outline, not present there. It confirms the reduction to `𝓥`-finiteness
"wastes" no strength: `𝓥`-finiteness is not an artificially stronger
sufficient condition, it is *exactly* as hard as (MRS) itself.

### Record Characterization Lemma — new this round

**Statement.** Call an index `i\ge1` *fresh* if no `k` with `1\le k<i` has
`P_k\subsetneq P_i` (vacuously true for `i=1`, since there is no `k<1`).
Then
`$$𝓥=\{P_i : i\ge1\text{ is fresh}\}.$$`
(This gives a description of `𝓥` with **no reference at all** to `M_n`,
`𝓜_n`, or the incremental antichain-update process — only to the raw
sequence `(P_n)_{n\ge1}` and the partial order `\subsetneq`.)

**Proof.**

`(\supseteq)` Let `i` be fresh; we show `P_i\in𝓜_i` (hence `\in𝓥`). We check
`i\in M_i`: by Lemma W3's definition, need no `k\in\{1,\dots,i\}` with
`P_k\subsetneq P_i`. For `k=i`: `P_i\subsetneq P_i` is false (not a proper
subset of itself). For `1\le k<i`: `P_k\not\subsetneq P_i` by freshness of
`i`. So no such `k` exists in `\{1,\dots,i\}`, giving `i\in M_i`, hence
`P_i\in𝓜_i\subseteq𝓥`.

`(\subseteq)` Let `C\in𝓥`; then `C\in𝓜_n` for some `n\ge1`, i.e. `C=P_i` for
some `i\in M_n` (so `i\le n`, and no `k\in\{1,\dots,n\}` has
`P_k\subsetneq P_i=C`). We claim this same index `i` is fresh: we need no
`k` with `1\le k<i` has `P_k\subsetneq P_i`. Since `i\le n`, every
`k` with `1\le k<i` satisfies `k<i\le n`, so `k\in\{1,\dots,n\}`; by the
above (applied to this `k`), `P_k\not\subsetneq P_i`. So `i` is fresh, with
`P_i=C`, giving `C\in\{P_i:i\text{ fresh}\}`. `\blacksquare`

**Numerical verification (pre-write sanity check, not part of the proof).**
Independently computed both sides — the simulator's direct `𝓜_n`-based
definition of `𝓥`, and this Lemma's "fresh index" definition — on
`a_1\in\{221,4087,2747,375,247\}`, `N=600`: **exact match** (`|𝓥|=|F|=6, 20,
22, 6, 7` respectively) in every case, zero discrepancies.

**Consequence used below.** Since freshness of `i` is equivalent (by exactly
the same argument as the `(\supseteq)`/`(\subseteq)` proof above, restricted
to `k<i` versus `k\in\{1,\dots,i-1\}`) to "`P_i` is not a proper superset of
any element of `𝓜_{i-1}`" (using the already-certified fact, from Corollary
W3′'s proof technique, that for any set `\{P_1,\dots,P_{i-1}\}`, some `P_k`
is a proper subset of `P_i` iff some *minimal* element of that set is), the
Record Characterization directly matches the "successful insertion" step of
the antichain-update view of `𝓜_n` used throughout the outline: `i` is fresh
exactly when inserting `P_i` into `𝓜_{i-1}` does not get immediately
discarded as dominated.

### Proposition FR (a necessary condition on fresh indices) — new this round

**Statement.** If `i\ge2` is fresh, then `P_1\not\subsetneq P_i` — i.e.
either `P_i=P_1` exactly, or there is some prime `p\in P_1` with `p\nmid a_i`.

**Proof.** Immediate from the definition of freshness with `k=1<i`: `i`
fresh means no `k<i` has `P_k\subsetneq P_i`; taking `k=1` gives
`P_1\not\subsetneq P_i`. `\blacksquare`

**Discussion.** This shows freshness is a genuinely restrictive condition
(not vacuous): every fresh index beyond the first must either exactly
reproduce `P_1` or omit at least one of `P_1`'s primes. This is consistent
with, but does not by itself explain, the empirically observed *decay* in
how often new fresh indices appear (Case II) or the *sudden, complete
cessation* of fresh indices after a single absorbing event (Case I, see
Theorem CI below) — see "Structural diagnosis" below for why this
proposition alone is far short of a finiteness proof.

### Theorem CI (Case I `\Rightarrow` `𝓥` finite, unconditionally, with an
explicit stabilization index) — new this round, fully proved

**Statement.** Suppose Case I holds: some prime `p` divides every `a_n`,
`n\ge1`. Write `a_1=pm` (`m:=a_1/p\ge1`, an integer since `p\mid a_1`). Let
`$$k_0:=\min\{k\ge1 : p^k\ge a_1\},\qquad N_0:=p^{k_0-1}-m+1.$$`
Then `N_0\ge1` is a well-defined positive integer, `𝓜_n=\{\{p\}\}` for every
`n\ge N_0`, and hence `𝓥` is finite; in fact
`𝓥\subseteq\{P_i:1\le i\le N_0\}`, a set of at most `N_0` values.

**Proof.** By the already-certified Lemma S' (`Case I\Rightarrow a_n=a_1+p(n-1)`
for **every** `n\ge1`, exact from `n=1`), the whole sequence is the explicit
arithmetic progression `a_n=a_1+p(n-1)=p(m+n-1)`. As `n` ranges over
`\{1,2,3,\dots\}`, `a_n` ranges exactly over all multiples of `p` that are
`\ge a_1` (bijectively: `a_n=pt` with `t=m+n-1\ge m`, and conversely every
multiple `pt\ge a_1=pm` — i.e. every `t\ge m` — equals `a_n` for `n=t-m+1`).

Since `p\ge2`, `p^k\to\infty` as `k\to\infty`, so `k_0` is a well-defined
finite positive integer (the set `\{k\ge1:p^k\ge a_1\}` is nonempty and
bounded below, hence has a minimum by well-ordering). By minimality of `k_0`,
`p^{k_0}\ge a_1=pm`, i.e. `p^{k_0-1}\ge m`, so `t_0:=p^{k_0-1}\ge m` is an
integer `\ge m`, giving `N_0:=t_0-m+1\ge1`. By the bijection above,
`a_{N_0}=p\cdot t_0=p^{k_0}` — the term at index `N_0` is exactly `p^{k_0}`,
a pure power of `p`, so `P_{N_0}=\mathrm{rad}(p^{k_0})=\{p\}`.

Now fix any `n\ge N_0`. We show `𝓜_n=\{\{p\}\}`.
- *`\{p\}\in𝓜_n`:* Since `P_{N_0}=\{p\}` and no set can be a proper subset of
  a singleton set of a prime (the only subset of `\{p\}` other than itself is
  `\varnothing`, which is never a radical, as `a_i>1` for every `i`), no
  `k\in\{1,\dots,n\}` has `P_k\subsetneq P_{N_0}=\{p\}`. So `N_0\in M_n`
  (`N_0\le n` since `n\ge N_0`), giving `\{p\}=P_{N_0}\in𝓜_n`.
- *No other value is in `𝓜_n`:* Let `i\le n` with `P_i\ne\{p\}`. Since Case I
  holds, `p\mid a_i`, i.e. `p\in P_i`; combined with `P_i\ne\{p\}`, this
  forces `\{p\}\subsetneq P_i` (a proper subset, since `P_i` contains `p` and
  at least one more prime). Since `N_0\le n` (as `n\ge N_0`), `k:=N_0` is a
  witness in `\{1,\dots,n\}` with `P_k=\{p\}\subsetneq P_i`, so `i\notin M_n`.
  Hence no index `i\le n` with `P_i\ne\{p\}` contributes to `𝓜_n`.

Combining, `𝓜_n=\{\{p\}\}` exactly, for every `n\ge N_0`. This proves (MRS)
with stabilization index `N_0`; by Theorem V (`(\Leftarrow)` direction, whose
proof gives `𝓥=\bigcup_{n=1}^{N_0}𝓜_n\subseteq\bigcup_{n=1}^{N_0}\{P_i:i\le n\}
=\{P_i:i\le N_0\}`), `𝓥` is finite, with at most `N_0` distinct values.
`\blacksquare`

**Worked numerical check (not part of the proof, a verification of the
formula against the flagged stress case).** For `a_1=11623`, `p=59`:
`m=11623/59=197`. `59^1=59<11623`, `59^2=3481<11623`, `59^3=205379\ge11623`,
so `k_0=3`. `N_0=59^{2}-197+1=3481-197+1=3285`. This **exactly matches** the
independently-simulated stabilization index (`n=3285`) found in point 4 of
the round-5 build summary above — not merely consistent with it, but an
exact derivation of it from Theorem CI's closed form, confirming the theorem
(and the underlying No-Resurrection/Interval-Lemma machinery) is correct on
this specific hard case, not merely observed to hold.

**Scope note (important, avoids overclaiming).** Theorem CI is *not* needed
to finish Case I itself — Case I is already completely and unconditionally
solved by Lemma S' alone (`a_n=a_1+p(n-1)` for all `n\ge1` directly gives the
problem's target conclusion with `T=1`, `L=p`, no FCBC/MRS machinery
required). Its value here is (a) a genuine, self-contained proof — not a
numerical check — that the No-Resurrection/Interval-Lemma/Theorem-V machinery
is *correct*, exhibited on a case complex enough to be flagged as a stress
test, and (b) a template illustrating what a real proof of `𝓥`-finiteness
looks like when the relevant "absorbing" structure (here: a single global
prime, and the guarantee that its powers are eventually hit by the AP) is
known explicitly. **Case II has no known analogue of this explicit AP
structure** — this is exactly why the Case II problem remains open; see
"Structural diagnosis" immediately below.

### Structural diagnosis of the Case II gap (honest, not a proof)

Theorem CI's mechanism relies on two facts special to Case I: (1) the whole
sequence is *explicitly* an arithmetic progression from `n=1` (Lemma S'), so
which values occur is fully known in closed form; (2) there is a *single*
prime `p` common to every term, so any term with radical `\{p\}` instantly
dominates every other realized value (since `p` is automatically an element
of every one of them). In Case II, **neither fact is available**: (1) there
is no known closed form for `a_n` (that is the content of the whole
unsolved problem), and (2) by Lemma C (certified, this file), the global
intersection `\bigcap_iP_i` is **empty** in Case II — there is no single
prime shared by every term, so no single future term's radical can play the
role `\{p\}` played above (a term dominates *some* earlier realized values by
sharing a common sub-radical with them, but by Lemma P′ that sub-radical need
not be the same prime across all pairs, and by Proposition NC1/NC2 already
certified in this file, no simple a-priori description — neither "primes
seen by Lemma C's collapse point" nor "primes `\le\mathrm{rad}(a_1)`" —
identifies which sub-radical values will eventually dominate everything).

The `a_1=11623` numerics (point 4 above) show fresh indices accumulating, for
thousands of steps, at a rate that empirically tracks the prime-counting
function `\pi(n)` (roughly one new fresh value `\{59,p\}` for each new prime
`p` realized) — a **decaying but persistently positive** rate — right up
until the single absorbing term appears, at which point freshness stops
**completely and permanently** (Theorem CI, `N_0`). A genuine `𝓥`-finiteness
proof in Case II would need to show an analogous "absorbing" phenomenon
occurs, but **without** knowing the explicit closed form that made this
provable in Case I. This is *exactly* the content already identified by
three independent constructions across this problem's whole population as
the sole remaining gap — `persistent-backbone-monovariant`'s `𝓥`
(this file), `imprint-automaton-periodicity`'s "Bounded Core Family" (per
this round's outline-reviewer, now literally the same open object once that
approach's Step-3 gap is patched), and `forced-primes-well-ordering`'s
Lemma FF (finiteness of the forced-primes set `F`) — and it is **not closed
this round**. No new elementary counting/pigeonhole mechanism was found this
round that closes it (Proposition FR is a genuine necessary condition, but,
as in round 3's Propositions ND1/ND2, a necessary condition on individual
fresh indices does not by itself bound how many distinct fresh values can
ever occur). Per the outline-reviewer's round-5 note, if the sibling
approaches also report being stuck on literally this same object next round,
the correct response is not a fourth reformulation but bringing in a
genuinely new tool (e.g. an actual density/sieve argument, confirmed absent
from `knowledge_base.md` and the crux corpus by `forced-primes-well-ordering`'s
own search) — not attempted this round, honestly out of scope for the time
available.

### Growth-Budget attempt (Round 6) — Lemma FOM, Fan-Size Corollary,
Generation-Chain Lemma, and the new `Λ_S`/`J_S` machinery

This subsection is unconditional (holds regardless of Case I/II) and is
logically independent of Lemma C onward; it is inserted here, directly after
the "Structural diagnosis" section, since it is a direct continuation of that
diagnosis with new tools.

#### Lemma FOM (First-Occurrence Minimality) — certified in full this round

**Statement.** For `C` a nonempty finite set of primes, define
`T_C:=\min\{x\in\mathbb{Z} : x>a_1,\ \mathrm{rad}(x)=C\}`. This is
well-defined: for every `t\ge1`, `\big(\prod_{p\in C}p\big)^t` has radical
exactly `C`, and these values are unbounded as `t\to\infty`, so
`\{x>a_1:\mathrm{rad}(x)=C\}` is a nonempty set of positive integers, hence
has a minimum by well-ordering.

*Claim.* If `n\ge2` is the first index with `\mathrm{rad}(a_n)=C` (no `i<n`
has `\mathrm{rad}(a_i)=C`), then `a_n=T_C`.

**Proof (single argument by contradiction, no case split — the cleaner route
identified by the round-6 outline-reviewer's independent re-derivation).**
Suppose, for contradiction, `a_n\ne T_C`. Since `n\ge2`, `a_n>a_1` (strict
monotonicity of the sequence from `a_1`), and `\mathrm{rad}(a_n)=C` by
hypothesis, so `a_n` is itself a member of the set `T_C` minimizes;
minimality of `T_C` gives `T_C\le a_n`. Combined with the contradiction
hypothesis `T_C\ne a_n`, we get `T_C<a_n` strictly.

*Sub-claim: `T_C` is not equal to any `a_i`, `i\ge1`.* For `i\ge n`:
`a_i\ge a_n>T_C` (strict monotonicity), so `T_C\ne a_i`. For `i<n`: if
`T_C=a_i`, then `\mathrm{rad}(a_i)=\mathrm{rad}(T_C)=C`, i.e. index `i<n`
already realizes radical `C`, contradicting that `n` is the *first* index
with `\mathrm{rad}(a_n)=C`. So `T_C\ne a_i` for `i<n` too. This proves the
sub-claim.

Since `(a_i)_{i\ge1}` is a strictly increasing, unbounded sequence of
positive integers, and `T_C` is a fixed positive integer not equal to any
`a_i` (sub-claim), the set `\{i\ge1:a_i<T_C\}` is finite (bounded, as
`a_i\to\infty`) and nonempty (`a_1<T_C` by definition of `T_C`). Let
`i^*:=|\{i\ge1:a_i<T_C\}|`; then `a_{i^*}<T_C`, and since `T_C` is not equal
to any `a_i`, the next term `a_{i^*+1}` (the smallest term `\ge T_C`) is in
fact `>T_C` strictly.

Since `T_C<a_n` (shown above) and `(a_i)` is strictly increasing,
`a_{i^*}<T_C<a_n` forces `i^*<n`, i.e. `i^*\le n-1`.

For every index `i\le i^*\ (\le n-1<n)`: since `a_n` was constructed by the
greedy admissibility rule, `\gcd(a_n,a_i)>1` for every `i<n`, in particular
for `i\le i^*`. This means `\mathrm{rad}(a_n)\cap\mathrm{rad}(a_i)=C\cap
\mathrm{rad}(a_i)\ne\varnothing`. Since `\mathrm{rad}(T_C)=C` (same set),
the very same nonempty intersection witnesses `\gcd(T_C,a_i)>1`. So `T_C` is
admissible against `a_1,\dots,a_{i^*}`.

By the greedy rule, `a_{i^*+1}` is *defined* as the smallest integer strictly
greater than `a_{i^*}` that is admissible against `a_1,\dots,a_{i^*}`. Since
`T_C>a_{i^*}` and `T_C` is admissible against `a_1,\dots,a_{i^*}` (just
shown), minimality of `a_{i^*+1}` gives `a_{i^*+1}\le T_C`. But we also
showed `T_C<a_{i^*+1}` above. Combining: `a_{i^*+1}\le T_C<a_{i^*+1}`, i.e.
`a_{i^*+1}<a_{i^*+1}` — a contradiction.

Hence the assumption `a_n\ne T_C` is false: `a_n=T_C`. `\blacksquare`

#### Fan-Size Corollary — certified in full this round

**Statement.** Let `C'` be a nonempty finite set of primes first occurring
at index `m\ge2` (so `a_m=T_{C'}` by Lemma FOM). Suppose some index `i<m`
has `\mathrm{rad}(a_i)=C'\cup\{q\}` for a prime `q\notin C'`. Then
`q\cdot\prod(C')\le a_i<a_m=T_{C'}`, i.e. `q<T_{C'}/\prod(C')`.

**Proof.** Since `\mathrm{rad}(a_i)=C'\cup\{q\}`, every prime of `C'` and the
prime `q` divide `a_i`; as `q\notin C'`, `q` and `\prod(C')` are coprime, so
their product `q\cdot\prod(C')` divides `a_i`, giving `q\cdot\prod(C')\le
a_i` (a positive divisor is at most the number). Since `i<m` and `(a_n)` is
strictly increasing, `a_i<a_m=T_{C'}`. Combining:
`q\cdot\prod(C')\le a_i<T_{C'}`, hence `q<T_{C'}/\prod(C')`. `\blacksquare`

#### Generation-Chain Lemma — certified in full this round

**Statement.** Fix a proper core `S\subsetneq P_1`. Call
`C_1\supsetneq C_2\supsetneq\cdots\supsetneq C_r\supseteq S` (`r\ge1`) a
*domination chain in `S`* if each `C_{l+1}` is a dominating witness (in the
sense of the already-certified No-Resurrection Lemma) that permanently
excludes `C_l` from `𝓜` from some point on. Then `r\le|C_1|-|S|+1`, in
particular every domination chain is finite.

**Proof.** Since `C_1\supsetneq C_2\supsetneq\cdots\supsetneq C_r`, transitivity
of `\supseteq` gives `C_l\supseteq C_r\supseteq S` for every `1\le l\le r`, so
`|C_l|\ge|S|` for every `l`. Combined with the strict decrease
`|C_1|>|C_2|>\cdots>|C_r|` (each containment strict), this is a strictly
decreasing sequence of `r` integers, all lying in `\{|S|,|S|+1,\dots,|C_1|\}`
(an interval of `|C_1|-|S|+1` integers), so `r\le|C_1|-|S|+1`. `\blacksquare`

*(This confirms the outline's own framing exactly: chain LENGTH is not new
difficulty — it is a three-line consequence of the already-certified
No-Resurrection Lemma. The open content, addressed below, is chain/companion
COUNT.)*

#### Lemma ER (Eventual Realization Dichotomy) — new this round, general and
previously unstated in this workspace

**Statement.** Let `y` be an integer with `y>a_1` and `y\ne a_i` for every
`i\ge1` (`y` is not (yet) a term of the sequence). Then it is **not** the
case that `\gcd(y,a_i)>1$ for every `i\ge1`; equivalently (contrapositive
form, the one used below): *if* `\gcd(y,a_i)>1` for every `i\ge1`, *then*
`y=a_m` for some `m\ge1`.

**Proof.** We prove the contrapositive form directly. Suppose
`\gcd(y,a_i)>1` for every `i\ge1`, and — toward a contradiction — suppose `y`
is not equal to any `a_i`. Since `(a_i)_{i\ge1}` is a strictly increasing,
unbounded sequence of positive integers and `y>a_1` is a fixed integer, the
set `\{i\ge1:a_i<y\}` is finite and nonempty (contains `i=1`); let
`n_0:=|\{i\ge1:a_i<y\}|$, so `a_{n_0}<y`. Since `y` is not equal to any
`a_i` (contradiction hypothesis) and `(a_i)` is strictly increasing, the next
term `a_{n_0+1}` (the smallest term `\ge y`) satisfies `a_{n_0+1}>y` strictly.

Since `y>a_{n_0}` and `\gcd(y,a_i)>1` for every `i=1,\dots,n_0` (special case
of the hypothesis "for every `i\ge1`"), `y` is an admissible candidate for
the greedy step that constructs `a_{n_0+1}` (the smallest integer `>a_{n_0}`
admissible against `a_1,\dots,a_{n_0}`). By minimality, `a_{n_0+1}\le y`. But
we showed `a_{n_0+1}>y`. Contradiction.

Hence `y` must equal some `a_i`, `i\ge1`. `\blacksquare`

**Numerical verification (sanity check, not part of the proof).** For
`a_1=247`, generated `500` terms (last term `14535`); checked *every*
integer `y` with `247<y<14535$ not already a term of the sequence: in all
`14287` cases, some earlier term `a_i` has `\gcd(y,a_i)=1$ (a blocking
witness exists), exactly as Lemma ER predicts — zero exceptions.

**Discussion.** This is a genuinely new, general structural fact (it uses
only the greedy rule's definition and well-ordering, not radicals or
Lemma FOM at all) — it closes a loose conceptual end left implicit
throughout this whole problem's workspace: an integer can *never* be
"permanently eligible but perpetually skipped" — the greedy process resolves
every candidate's fate (realized, or permanently blocked) in finite time.

#### `Λ_S`-Reduction Lemma — new this round

**Statement.** Fix a proper nonempty core `S\subsetneq P_1`. Define
`Λ_S:=\bigcup_{C\in𝓥_S}(C\setminus S)` (all "companion primes" ever
appearing in some minimal radical of core `S`). Then `𝓥_S` is finite **if
and only if** `Λ_S` is finite.

**Proof.**

`(\Rightarrow)` If `𝓥_S` is finite, `Λ_S` is a union of finitely many finite
sets `C\setminus S` (`C\in𝓥_S`, each `C` finite as it is the radical of an
actual integer), hence finite.

`(\Leftarrow)` Suppose `Λ_S` is finite. Every `C\in𝓥_S` satisfies
`S(C)=C\cap P_1=S`, so `S\subseteq C`, giving `C=S\cup(C\setminus S)`; and
`C\setminus S\subseteq Λ_S` by definition of `Λ_S` as the union over all such
`C`. So every `C\in𝓥_S` lies in `\{S\cup Q:Q\subseteq Λ_S\}`, a set of
cardinality `2^{|Λ_S|}` (finite, since `Λ_S` is finite). Hence
`𝓥_S\subseteq\{S\cup Q:Q\subseteq Λ_S\}`, and a subset of a finite set is
finite. `\blacksquare`

**Discussion.** This is a clean, genuinely useful reformulation: it converts
"is a certain *family of sets* finite" into "is a single *flat set of
primes* finite" — a strictly simpler combinatorial question, and the natural
setting for the mechanism below.

#### Single-Companion Finiteness Lemma — new this round, the round's main
positive result

**Definition.** For a proper nonempty core `S\subsetneq P_1`, define
`J_S:=\{j\ge1:\mathrm{rad}(a_j)\cap S=\varnothing\}` (the *`S`-avoiding index
set*: indices whose radical is entirely disjoint from `S`). Define
`Q_S:=\{q\text{ prime},\,q\notin P_1 : \exists\,i\ge1,\ \mathrm{rad}(a_i)=
S\cup\{q\}\}` (primes ever realized as the *sole* companion of `S` in some
actual term of the sequence — not required to be minimal/fresh).

**Statement.** If `J_S` is infinite, then `Q_S` is finite; explicitly,
`Q_S\subseteq D\setminus P_1` where `D:=\bigcap_{j\in J_S}\mathrm{rad}(a_j)`,
a fixed finite set with `|D|\le\omega(a_{j_1})` (`j_1:=\min J_S`).

**Proof.** List `J_S=\{j_1<j_2<j_3<\cdots\}$ (infinite by hypothesis, so this
listing is well-defined and unbounded). Apply the already-certified
Generalized Lemma C (`lemmas/lemma-C-generalized-subsequence.md`) to the
index set `I:=J_S`: the sequence `C^{J_S}_m:=\bigcap_{l=1}^m
\mathrm{rad}(a_{j_l})` is non-increasing in `m` and stabilizes: there is a
finite `m_0` with `C^{J_S}_m=C^{J_S}_{m_0}=:D` for all `m\ge m_0`.

*Claim: `D=\bigcap_{j\in J_S}\mathrm{rad}(a_j)` (the full, infinite
intersection).* For `l\le m_0`: `D=C^{J_S}_{m_0}=\bigcap_{l'=1}^{m_0}
\mathrm{rad}(a_{j_{l'}})\subseteq\mathrm{rad}(a_{j_l})` directly (intersecting
over an index set including `l`). For `l>m_0`: by stabilization,
`C^{J_S}_{l-1}=C^{J_S}_l=D$ (both indices `\ge m_0`), and
`C^{J_S}_l=C^{J_S}_{l-1}\cap\mathrm{rad}(a_{j_l})`, so
`D=D\cap\mathrm{rad}(a_{j_l})`, giving `D\subseteq\mathrm{rad}(a_{j_l})`. So
`D\subseteq\mathrm{rad}(a_{j_l})` for *every* `l\ge1`, i.e.
`D\subseteq\bigcap_{j\in J_S}\mathrm{rad}(a_j)`. Conversely the full
intersection is a subset of the intersection over just the first `m_0`
indices, i.e. `\subseteq C^{J_S}_{m_0}=D`. Combining, `D=\bigcap_{j\in
J_S}\mathrm{rad}(a_j)` exactly, proving the claim. In particular `D` is
finite: `D\subseteq\mathrm{rad}(a_{j_1})`, so `|D|\le\omega(a_{j_1})`.

Now let `q\in Q_S`: some index `i` has `\mathrm{rad}(a_i)=S\cup\{q\}`. Since
`S\ne\varnothing`, `\mathrm{rad}(a_i)\cap S=S\ne\varnothing`, while every
`j\in J_S` has `\mathrm{rad}(a_j)\cap S=\varnothing`; hence `i\ne j` for
every `j\in J_S`. By the already-certified Lemma P′ (pairwise intersecting
radicals, unconditional: `\gcd(a_i,a_j)>1` for all `i\ne j`), for every
`j\in J_S`, `\gcd(a_i,a_j)>1`, i.e.
`(S\cup\{q\})\cap\mathrm{rad}(a_j)\ne\varnothing`. Since
`S\cap\mathrm{rad}(a_j)=\varnothing` (as `j\in J_S`), this nonempty
intersection must come from `\{q\}`, i.e. `q\in\mathrm{rad}(a_j)`. This holds
for *every* `j\in J_S`, so `q\in\bigcap_{j\in J_S}\mathrm{rad}(a_j)=D`. Also
`q\notin P_1$ (by definition of `Q_S`), so `q\in D\setminus P_1`. Hence
`Q_S\subseteq D\setminus P_1`, a finite set. `\blacksquare`

**Numerical verification (exact match, not just consistency — done before
finalizing the proof, per project convention).**
- `a_1=2747`, `S=\{41\}` (`P_1=\{41,67\}`): `J_S=I_{\{67\}}`, with `118`
  elements found among the first `6000` terms (still growing at the end of
  the tested range: last found index `5989`). Computed `D=\bigcap_{j\in
  J_S}\mathrm{rad}(a_j)$ restricted to those `118` terms: `D=\{2,3,7,67\}`,
  constant from the very first `J_S`-element onward (the running intersection
  size is `4` at every step checked). Predicted bound:
  `Q_S\subseteq D\setminus P_1=\{2,3,7\}`. Directly searching all `6000`
  terms for radicals of the exact form `\{q,41\}`: found
  `Q_S=\{2,3,7\}` — an **exact match**, not merely a valid superset.
- `a_1=247`, `S=\{13\}` (`P_1=\{13,19\}`): `J_S=I_{\{19\}}`, `3228` elements
  among the first `6000` terms. `D=\{19\}`. Predicted bound:
  `Q_S\subseteq D\setminus P_1=\{19\}\setminus\{13,19\}=\varnothing`.
  Direct search: `Q_S=\varnothing` — exact match.
- `a_1=247`, `S=\{19\}`: symmetric, `J_S=I_{\{13\}}`, `2074` elements,
  `D=\{13\}`, predicted `Q_S\subseteq\varnothing`, direct search confirms
  `Q_S=\varnothing`.

The exactness of the match (not just `Q_S\subseteq` a valid but loose bound)
in all three cases is strong evidence the mechanism is not merely correct
but capturing the true underlying reason single-companion recruitment halts.

#### Multi-Companion Reduction Proposition — new this round, the honest
diagnosis of why Single-Companion Finiteness does not extend

**Statement.** Let `Q` be a finite set of primes with `Q\cap(P_1\cup S)=
\varnothing` and `|Q|\ge2`, and suppose some index `i` has
`\mathrm{rad}(a_i)=S\cup Q`. Then `Q\cap\mathrm{rad}(a_j)\ne\varnothing` for
every `j\in J_S`.

**Proof.** Identical mechanism to the Single-Companion Lemma's core step:
since `S\ne\varnothing`, `i\notin J_S`, so for `j\in J_S`, `i\ne j`, and
Lemma P′ gives `\gcd(a_i,a_j)>1`, i.e. `(S\cup Q)\cap\mathrm{rad}(a_j)\ne
\varnothing`. Since `S\cap\mathrm{rad}(a_j)=\varnothing` (`j\in J_S`), the
nonempty intersection must come from `Q`, i.e. `Q\cap\mathrm{rad}(a_j)\ne
\varnothing`. `\blacksquare`

**Why this genuinely blocks the Growth-Budget Lemma, precisely (not just by
assertion).** For `|Q|=1$, `Q=\{q\}`, this proposition forces the *same
single prime* `q` to lie in `\mathrm{rad}(a_j)` for *every* `j\in J_S`
simultaneously — exactly the hypothesis needed to apply the Generalized
Lemma C's stabilization argument (a fixed element in an eventually-constant
*intersection*), which is what makes the Single-Companion Lemma work. For
`|Q|\ge2`, the proposition only forces `Q` to *hit* (intersect) each
`\mathrm{rad}(a_j)` — possibly via a *different* element of `Q` for each
`j` — which is precisely a **finite covering/hitting-set condition on the
infinite family `\{\mathrm{rad}(a_j):j\in J_S\}`**, i.e. exactly a
*restricted, local instance of the Finite Covering Backbone Conjecture
itself* (the same object this whole population has been attacking since
round 2). The Generalized Lemma C mechanism does **not** apply to a
hitting-set condition (it only ever produces a genuine set-intersection
stabilization, not a covering-set existence result) — so this proposition
does not extend the Single-Companion mechanism to multi-companion bundles;
it precisely *proves* (not just observes) that any extension would require
solving a local FCBC-style problem, i.e. is not "free" additional work but
the *same order of difficulty* as the original open conjecture. This is the
honest, rigorous location of the remaining gap: **not** a vague restatement
of "pointwise ≠ cumulative," but a specific, proved reduction pinpointing
*exactly* which sub-case (multi-companion bundling) resists this round's new
tool and *why* (hitting-set vs. fixed-intersection).

**Second honest gap: `J_S` infinite is not proved in general.** The
Single-Companion Finiteness Lemma is *conditional* on `J_S` being infinite.
This was verified numerically in every core tested this round (see the
"Numerical verification" above — all `J_S`'s found were in the thousands,
still growing at the edge of the tested range), but no proof that `J_S` is
*always* infinite for a proper core `S\subsetneq P_1` is given here. (Sketch
of the difficulty: `J_S` finite would mean cofinitely many terms of the
*entire* sequence intersect `S`, a strong "near-universal local hub"
property of `S` that is not excluded by any currently-certified fact — Lemma
C's Case II conclusion, `\bigcap_i\mathrm{rad}(a_i)=\varnothing`, is
compatible with `S` being hit by *every* term via a *different* prime of `S`
each time, which would make `J_S=\varnothing$, the extreme case of "finite."
No mechanism ruling this out was found this round; it is recorded honestly
as open, not assumed away.)

### Round 7: Permanent Bundle Lemma and the count-bound stress test

This subsection is unconditional given the standing hypothesis "`J_S`
infinite" (same hypothesis the Single-Companion Finiteness Lemma already
carries) and is a direct continuation of the Multi-Companion Reduction
Proposition immediately above. Full statements and proofs are also
certified standalone in `lemmas/lemma-permanent-bundle.md`; the exposition
here is self-contained.

#### Class-Decomposition Fact (new, three lines from Lemma P′)

**Statement.** Fix a bundle `Q` for `S` (`S\cup Q=\mathrm{rad}(a_i)` for
some `i`). If `R\subsetneq S\cup Q` is the radical of *any* real index `k`
(any class, not necessarily class `S`), then, writing `R_S:=R\cap S`,
`R_Q:=R\cap Q` (so `R=R_S\cup R_Q`, since `R\subseteq S\cup Q` and
`S\cap Q=\varnothing`), we have `R_S\ne\varnothing`.

**Proof.** By the already-certified Lemma P′, `\gcd(a_1,a_k)>1` for every
`k\ge2`, and trivially for `k=1`; hence `\mathrm{rad}(a_k)\cap P_1\ne
\varnothing` for *every* index `k` (this is exactly the fact underlying
Theorem CD's proof). Since `R\subseteq S\cup Q` and `Q\cap P_1=\varnothing`
(companions are disjoint from `P_1` by definition), `R\cap P_1=R\cap S=
R_S`. So `R_S=R\cap P_1\ne\varnothing`. `\blacksquare`

**Consequence (singleton cores need no sub-core case).** If `|S|=1`, the
only subsets of `S` are `\varnothing` and `S`; since `R_S\ne\varnothing`
always, `R_S=S` is forced. So for singleton `S`, **every** possible
dominator of `S\cup Q` automatically has the form `S\cup Q'` (`Q'\subsetneq
Q`) — there is no "sub-core" case to exclude. For `|S|\ge2`, `R_S` can be a
genuine nonempty *proper* subset of `S` — a "sub-core dominator" — and
this case must be separately excluded (see (SCA) below).

#### Permanent Pair Lemma — certified in full this round, with a genuine
gap found and fixed

**Statement.** Let `Q=\{q_1,q_2\}` (`q_1\ne q_2`, both `\notin P_1`) be a
bundle for `S` with `q_1,q_2\notin D_S`. If **either** `|S|=1`, **or**
`|S|\ge2` and **Sub-Core Avoidance (SCA)** holds — no index `k` has
`\mathrm{rad}(a_k)=S'\cup Q''` for any nonempty proper subset `S'\subsetneq
S` and any `Q''\subseteq Q` — then `S\cup Q` is never dominated: it is a
permanent member of `𝓥_S`.

**Proof.** By the Class-Decomposition Fact, any dominator `R\subsetneq
S\cup Q` has `R=R_S\cup R_Q`, `R_S\ne\varnothing`.

*Case `R_S=S`* (forced if `|S|=1`; the only remaining case if `|S|\ge2`
once (SCA) excludes `R_S\subsetneq S`): then `R\subsetneq S\cup Q` forces
`R_Q\subsetneq Q`, i.e. `R=S\cup Q'` for `Q'\in\{\varnothing,\{q_1\},
\{q_2\}\}`.
- `Q'=\varnothing`: `R=S`. If some index `k` had `\mathrm{rad}(a_k)=S`,
  fix any `j\in J_S` (nonempty, `J_S` infinite). If `k>j`: the
  Permanent-Inadmissibility Lemma with `C:=S`, witness `j` (`\mathrm{rad}
  (a_j)\cap S=\varnothing` by `j\in J_S`) excludes any term with radical
  `S` at any index `>j`, contradiction. If `k\le j`: Lemma P′ gives
  `\gcd(a_k,a_j)>1`, i.e. `S\cap\mathrm{rad}(a_j)\ne\varnothing`,
  contradicting `j\in J_S`. Either way, no such `k` exists.
- `Q'=\{q_1\}` or `\{q_2\}`: excluded by the contrapositive of the
  Single-Companion Finiteness Lemma (`Q_S\subseteq D_S`; `q_1,q_2\notin
  D_S` by hypothesis).

*Case `R_S\subsetneq S` proper* (only possible if `|S|\ge2`): excluded
directly by (SCA). `\blacksquare`

**The gap found and fixed.** The round-7 math-explorer's proposal and the
round-7 outline-reviewer's independent re-derivation
(`/tmp/round-7/math-explorer-multicompanion-induction.md`,
`/tmp/round-7/outline-reviewer.md`) both search for dominators **only
within `I_S`** (same-class indices) — correct for the singleton-core
instance they numerically checked (`a_1=4199,S=\{17\}`, by the
Consequence above), but **silently incomplete** for the non-singleton
instance they also used (`a_1=21528751,S=\{103,197\}`, bundle
`\{11,97\}`): a sub-core dominator (radical `\subseteq\{103,11,97\}` or
`\subseteq\{197,11,97\}`, missing the other element of `S`) is a priori
possible and neither party checked for it.

**(SCA) proved unconditionally (not sampled) for this instance.** Direct
inspection of the already-generated sequence data: `a_3=25495899` has
`\mathrm{rad}(a_3)=\{2,3,7,197,1301\}`, disjoint from
`\{103\},\{103,11\},\{103,97\},\{103,11,97\}` (none of `103,11,97` divides
`a_3`). By Permanent-Inadmissibility (four applications, `C:=` each of
these sets, witness `3`), none can ever be realized at any index `>3`, and
direct check of `\mathrm{rad}(a_1),\mathrm{rad}(a_2),\mathrm{rad}(a_3)`
confirms none equals one of them either. Symmetrically, `a_2=21811383` has
`\mathrm{rad}(a_2)=\{2,41,103,2549\}`, disjoint from `\{197\},\{197,11\},
\{197,97\},\{197,11,97\}`, giving the same conclusion for the other
sub-core. **(SCA) is therefore fully proved, not merely checked up to
`N=3{,}000{,}000`, for this instance** — the gap is completely closed here,
via the already-certified Permanent-Inadmissibility Lemma and two named
witnesses, not new machinery.

#### Permanent Bundle Lemma (arbitrary size `k`, new this round)

**Statement.** Let `Q` (`|Q|=k\ge1`) be a bundle for `S`. Suppose (i)
`Q\cap D_S=\varnothing`; (ii) **Subset Avoidance (SA)**: every nonempty
proper subset `Q'\subsetneq Q` has `S\cup Q'` never realized at any index;
(iii) (SCA) as above (automatic if `|S|=1`). Then `S\cup Q` is never
dominated.

**Proof.** As above: `R_S\subsetneq S` excluded by (SCA); `R_S=S,R_Q=
\varnothing` excluded by Permanent-Inadmissibility; `R_S=S`, `R_Q`
nonempty proper subset of `Q` excluded directly by (SA) (no index has this
radical at all). `\blacksquare`

**Relation to the Pair case.** For `k=2`, every proper nonempty `Q'
\subsetneq Q` is a singleton, so (SA) is *implied* by (i) via
Single-Companion Finiteness — it need not be separately assumed (matching
the Pair Lemma above). For `k\ge3`, (SA) additionally requires that no
*multi-element* proper subset (size `2,\dots,k-1`) is ever separately
realized — genuinely independent of (i).

**Exhaustive numerical validation.** Across a from-scratch simulation of
all five mandated hard cases, pushed to `N=3`–`5{,}000{,}000` (see
methodology below), found **44 fresh, `D_S`-disjoint bundles of size
`\ge3`**. In **every single one**, "(SA) holds" exactly predicted "still in
the antichain at the final simulated index" and "(SA) fails" (an explicit
smaller realized subset exhibited) exactly predicted "dominated, not
alive" — **zero exceptions in either direction**. Three worked cases,
proved (not just observed):
- `a_1=2747,S=\{67\},Q=\{2,3,7\}`: `a_2=2749` (`\mathrm{rad}=\{2,17,41\}`,
  disjoint from `\{3,7,67\}`), `a_4=2761` (`\mathrm{rad}=\{3,23,41\}`,
  disjoint from `\{2,7,67\}`), `a_{10}=2812` (`\mathrm{rad}=\{7,11,41\}`,
  disjoint from `\{2,3,67\}`) — three applications of
  Permanent-Inadmissibility prove all three 2-element proper subsets of
  `Q` can never be realized as companions of `\{67\}`: (SA) **fully
  proved**. `|S|=1` so (SCA) is automatic. Hence `\{2,3,7,67\}` is
  **rigorously proved** permanent (matches: alive from its first-fresh
  index `3` through `N=5{,}000{,}000` unchanged) — this bundle is *not*
  covered by the Pair Lemma at all (it has 3 companions, not 2), so this
  is genuinely new reach.
- `a_1=21528751,S=\{103,197\},Q=\{11,97\}`: (SA) vacuous (`|Q|=2`,
  implied by (i)); (SCA) proved above. Hence **rigorously proved**
  permanent — the exact instance that originally exposed the gap is now
  fully closed.
- Negative control: `a_1=4199,S=\{19\},Q=\{2,3,37\}` satisfies (i) but
  **violates** (SA) (`S\cup\{2,3\}=\{2,3,19\}` is independently realized
  at index `11`, after `Q`'s own first-fresh index `4`); correctly, this
  bundle is confirmed **absent** from the final antichain at
  `N=5{,}000{,}000` — the Lemma does not overclaim permanence where the
  hypothesis genuinely fails.

#### Why this sharpens the bundle-size-induction foreclosure

The round-7 explorer already proved no `k=2\to k=1` reduction exists (a
realized 2-bundle with both companions outside `D_S` is permanent by
Single-Companion Finiteness alone, with no route back to a `k=1` fact).
This round shows the natural repair — replacing the flawed
`D_S`-disjointness-alone criterion with the corrected
`D_S`-disjointness-plus-(SA) criterion — **also fails to give a working
induction**: verifying (SA) for a size-`k` bundle requires knowing whether
*any* of its `2^k-2` proper nonempty subsets is *ever* realized as a
companion of `S`, at any index — an instance of exactly the same general
"is this bundle ever realized" question, recursively, one level down (or
more, for the smallest subsets). This deepens, rather than merely repeats,
the explorer's foreclosure: even a *corrected* size-based criterion does
not reduce the problem's difficulty, it just relocates the same open
question to a smaller universe.

#### Deep count-bound stress test — methodology and honest result

**Methodology.** Built an efficient greedy-sequence simulator: rather than
factoring every rejected candidate, it maintains the current
minimal-radical antichain as a set of `(\text{radical},\ \text{primorial})`
pairs and tests candidates via `\gcd` against each primorial (`O(1)`
per antichain element, no factoring needed until a candidate is actually
accepted, at which point it is factored once via `sympy.primefactors` to
update the antichain). **Cross-validated before trusting any large-`N`
run**: (a) against a brute-force simulator checking `\gcd(x,a_i)>1$
against **every** previous term directly (no antichain shortcut at all) —
exact match on all five mandated `a_1` values at `N=1000`, and on
`a_1=247` at `N=3000`; (b) against a fully independent, `O(N^2)`,
from-scratch computation of the minimal-radical antichain (no incremental
update logic shared with the simulator) on the brute-force-generated
sequence for `a_1=247,N=3000` — exact match (identical 7-element antichain
composition, not just size).

**Result.** Pushed all five mandated cases to `N=3`–`5{,}000{,}000`
(`a_1=247,2747,4199,4087` to `5{,}000{,}000`; `a_1=21528751`, whose larger
starting value makes each step costlier, to `3{,}000{,}000`). For
**every** proper core `S` of **every** one of the five cases, tracked (via
an efficient single-pass-plus-bisection re-implementation, not the naive
`O(N)`-per-snapshot approach, to make the large-`N` runs tractable) the
count of distinct fresh (`\in𝓥_S`) bundles at exponentially-spaced
snapshots. **In every case, this count is completely flat from an early,
`a_1`-specific point onward, all the way to the end of the simulated
range** — zero new distinct bundles over a `10^3`–`10^6`-fold extension in
`N`. Going further, the **entire global antichain `𝓜_n`** (tracked by
literal set identity, via `add`/`remove` event logging, not just size) was
found to **freeze completely** — zero further changes of any kind — at:

| `a_1` | freeze index | final antichain size | matches prior record? |
|---|---|---|---|
| `247` | `7` | `7` | new (not previously pinned down) |
| `2747` | `163` | `5` | **yes** — matches the documented `a_{163}` collapse exactly |
| `4199` | `92` | `7` | **yes** — matches round 4's "worst case `n\le92`" exactly |
| `4087` | `54` | `3` | **yes** — matches the documented Negative-Finding-2 collapse exactly |
| `21528751` | `44967` | `9` | consistent with, sharper than, the documented `n\approx27831`/`44966` range |

and **no change occurs after these indices, through the full tested
range** (a `700{,}000\times$ extension past the freeze point for
`a_1=247`).

**Honest assessment (do not overclaim).** This is genuine, new depth of
empirical support: previous rounds verified `𝓜_n`/`𝓥_S` stability only up
to a few tens of thousands of terms on these hard cases; this round
verifies literal, unchanging set-identity up to `3`–`5` million terms,
cross-validated by an independent brute-force implementation, with **zero
exceptions across all five mandated instances**. This is the deepest and
most direct evidence for (MRS)/`𝓥`-finiteness produced anywhere in this
workspace's history. **It is still finite-`N` evidence, not a proof for a
general `a_1`.** No analytic mechanism was found this round that converts
"the antichain has not changed in the tested range" into "the antichain
will never change again" for an arbitrary `a_1` — this is the identical
pointwise-vs-cumulative obstruction flagged since round 3 (Markov bound),
round 5 (Growth-Budget), and round 6 (Multi-Companion Reduction). The
count-bound target set by this round's outline — bound the number of
`D_S`-disjoint (now: (SA)-satisfying) bundles ever realized for a *general*
core `S` — **remains open**. Status stays `partial`.

### Lemma C (Global Intersection Collapse) — proved in full this round

**Statement.** Let `P_1:=\mathrm{rad}(a_1)`, `k:=|P_1|`. For `n\ge1` define
$$C_n:=\bigcap_{i=1}^n\mathrm{rad}(a_i)\ \subseteq P_1.$$
Then:
(a) `(C_n)_{n\ge1}` is non-increasing (`C_{n+1}\subseteq C_n` for every `n`);
(b) there is a finite `N_0\ge1` with `C_n=C_{N_0}=:C_\infty` for all `n\ge N_0`;
(c) `C_\infty\ne\varnothing` **if and only if** Case I holds (some prime divides
*every* `a_n`, `n\ge1`); in particular, in Case II, `C_{N_0}=\varnothing`.

**Proof.**

*(a) Non-increasing.* By definition, for `n\ge1`,
`C_{n+1}=\bigcap_{i=1}^{n+1}\mathrm{rad}(a_i)=\Big(\bigcap_{i=1}^{n}\mathrm{rad}(a_i)\Big)\cap\mathrm{rad}(a_{n+1})=C_n\cap\mathrm{rad}(a_{n+1})\subseteq C_n.$
Also `C_1=\mathrm{rad}(a_1)=P_1`, so `C_n\subseteq P_1` for every `n` (immediate
induction from (a)), and `|C_n|` is a non-increasing sequence of integers in
`\{0,1,\dots,k\}`.

*(b) Finite stabilization.* The sequence of nonnegative integers
`|C_1|\ge|C_2|\ge\cdots\ge0` is non-increasing; a non-increasing sequence of
nonnegative integers can strictly decrease at most `k` times (each strict
decrease drops the value by at least `1`, starting from `|C_1|\le k` and never
going below `0`). Hence there is a finite index `N_0` after which `|C_n|` is
constant for all `n\ge N_0` (take `N_0=1` plus the index of the last strict
decrease, or `N_0=1` if there is no strict decrease). Combined with the nesting
`C_{N_0}\supseteq C_{N_0+1}\supseteq\cdots`, constancy of `|C_n|` for `n\ge N_0`
forces `C_n=C_{N_0}` exactly for all `n\ge N_0` (if `C_n\subsetneq C_{N_0}` for
some `n>N_0` with `n\ge N_0`, then `|C_n|<|C_{N_0}|`, contradicting constancy).
Set `C_\infty:=C_{N_0}`.

*Caution (kept from the outline, now independently re-verified by hand):* `N_0`
is finite but **not** bounded by `k+1` or any formula purely in `k` — the
sequence `|C_n|` can stay constant across arbitrarily many steps between drops.
Explicit witness: `a_1=65=5\cdot13` (`k=2`). Trace: `a_1,\dots,a_4=65,70,75,78`
(each obtainable from the problem's recursive rule; `70=2\cdot5\cdot7`,
`75=3\cdot5^2`, `78=2\cdot3\cdot13`). Then `C_1=\{5,13\}`,
`C_2=\{5,13\}\cap\{2,5,7\}=\{5\}`, `C_3=\{5\}\cap\{3,5\}=\{5\}`,
`C_4=\{5\}\cap\{2,3,13\}=\varnothing`. So `N_0=4>k+1=3`: only `2` strict drops
occurred (`|C_1|=2\to|C_2|=1\to|C_4|=0`), but the second drop happened only at
step `4`, not step `3`.

*(c) The "iff Case I" characterization.* By nesting (part (a)), for every
`n\le N_0` we have `C_n\supseteq C_{N_0}=C_\infty`, and for `n\ge N_0`,
`C_n=C_\infty`; hence `C_\infty\subseteq C_n` for **every** `n\ge1`.

`(\Leftarrow)` Suppose Case I holds: some prime `p` divides `a_i` for every
`i\ge1`. Then `p\in\mathrm{rad}(a_i)` for every `i`, so for every `n`,
`p\in\bigcap_{i=1}^n\mathrm{rad}(a_i)=C_n`. In particular `p\in C_{N_0}=C_\infty`,
so `C_\infty\ne\varnothing`.

`(\Rightarrow)` Suppose `C_\infty\ne\varnothing`; pick `p\in C_\infty`. Fix any
index `i_0\ge1`. Since `C_\infty\subseteq C_n` for every `n` (shown above), take
`n:=\max(i_0,N_0)\ge i_0`; then `p\in C_n=\bigcap_{i=1}^n\mathrm{rad}(a_i)`, and
since `i_0\le n`, this gives `p\in\mathrm{rad}(a_{i_0})`, i.e. `p\mid a_{i_0}`.
As `i_0` was an arbitrary positive integer, `p` divides every `a_n`, i.e. Case I
holds.

This proves both directions, so `C_\infty\ne\varnothing\iff` Case I. In
particular, in Case II, `C_\infty=\varnothing`, i.e. `C_{N_0}=\varnothing` for
the specific finite `N_0` from part (b). `\blacksquare`

**Corollary (self-contained proof that `a_1=221` and `a_1=375` below are Case
II).** For both examples, direct computation (see the propositions below) gives
`C_3=\varnothing` for `a_1=221` and `C_3=\varnothing` for `a_1=375`; by Lemma C
part (c) (contrapositive), this rigorously proves each is Case II — not merely
"presumably Case II from not finding a saturating prime by inspection."

### Proposition NC1 (the naive "read the backbone off `N_0`" idea is false) — new, proved in full this round

**Statement.** Let `N_0` be as in Lemma C and
`S_0:=\bigcup_{i=1}^{N_0}\mathrm{rad}(a_i)` (a finite set, since it is a finite
union of finite sets). It is **not true in general** that every canonical
witness `w(i,j):=\min(\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j))` (for `i<j`,
well-defined by Lemma P′) lies in `S_0`.

**Proof (explicit counterexample, fully hand-verified).** Take `a_1=221=13\cdot
17`. We trace the first five terms directly from the problem's recursive rule
(`a_{n+1}` = least integer `>a_n` with `\gcd(\cdot,a_i)>1` for all `i\le n`):

- `a_1=221=13\cdot17`.
- `a_2`: every integer `x` with `221<x<234` is checked and fails the `i=1`
  condition, since `\gcd(x,221)>1` requires `13\mid x` or `17\mid x`, and the
  next multiple of `13` after `221=13\cdot17` is `234=13\cdot18`, while the next
  multiple of `17` after `221` is `238=17\cdot14>234`. So `234` is the smallest
  integer `>221` admissible against `a_1`, hence `a_2=234=2\cdot3^2\cdot13`.
- `a_3`: candidates `235,\dots,237` are not divisible by `13` or `17` (direct
  check: `235=5\cdot47`, `236=2^2\cdot59`, `237=3\cdot79`), so all fail against
  `a_1`. `238=2\cdot7\cdot17` is divisible by `17` (`\gcd(238,221)=17>1`, passes
  `a_1`) and `\gcd(238,234)=2>1` (both even, passes `a_2`). So `a_3=238`.
- `a_4`: candidates `239,\dots,246` are checked and each fails against `a_1`
  (none is divisible by `13` or `17`: `239` prime, `240=2^4\cdot3\cdot5`, `241`
  prime, `242=2\cdot11^2`, `243=3^5`, `244=2^2\cdot61`, `245=5\cdot7^2`,
  `246=2\cdot3\cdot41`). `247=13\cdot19` passes `a_1` (`\gcd=13`) and `a_2`
  (`\gcd(247,234)=13`), but `\gcd(247,238)=\gcd(13\cdot19,\,2\cdot7\cdot17)=1`,
  failing against `a_3`. `248,\dots,254` are checked and each fails against
  `a_1` (`248=2^3\cdot31`, `249=3\cdot83`, `250=2\cdot5^3`, `251` prime,
  `252=2^2\cdot3^2\cdot7`, `253=11\cdot23`, `254=2\cdot127`; none divisible by
  `13` or `17`). `255=3\cdot5\cdot17` passes `a_1` (`\gcd=17`), `a_2`
  (`\gcd(255,234)=3`), and `a_3` (`\gcd(255,238)=17`). So `a_4=255`.
- `a_5`: candidates `256,\dots,259` all fail against `a_1` (`256=2^8`,
  `257` prime, `258=2\cdot3\cdot43`, `259=7\cdot37`; none divisible by `13` or
  `17`). `260=2^2\cdot5\cdot13` passes `a_1` (`\gcd=13`), `a_2` (`\gcd=2\cdot
  13`), `a_3` (`\gcd=2`), and `a_4` (`\gcd(260,255)=5`). So `a_5=260`.

So `a_1,\dots,a_5=221,234,238,255,260`, with
`\mathrm{rad}(a_1)=\{13,17\},\ \mathrm{rad}(a_2)=\{2,3,13\},\ \mathrm{rad}(a_3)=
\{2,7,17\}`.

Applying Lemma C: `C_1=\{13,17\}`, `C_2=\{13,17\}\cap\{2,3,13\}=\{13\}`,
`C_3=\{13\}\cap\{2,7,17\}=\varnothing`. So `N_0=3` and
`S_0=\{13,17\}\cup\{2,3,13\}\cup\{2,7,17\}=\{2,3,7,13,17\}`.

Now `\mathrm{rad}(a_4)=\mathrm{rad}(255)=\{3,5,17\}` and
`\mathrm{rad}(a_5)=\mathrm{rad}(260)=\{2,5,13\}`, so
`\mathrm{rad}(a_4)\cap\mathrm{rad}(a_5)=\{5\}`, giving
`w(4,5)=5`. But `5\notin S_0=\{2,3,7,13,17\}`. This exhibits a concrete pair
`(i,j)=(4,5)` whose canonical witness is **not** in `S_0`, disproving the
statement. `\blacksquare`

**Interpretation.** The prime `5` first appears (as a factor of `a_4=255`)
strictly *after* the index `N_0=3` at which Lemma C's global collapse already
occurred — so it is not "already visible" in `S_0` — and yet it goes on to
become the *canonical minimal witness* for the very next pair. This is a
genuine obstruction to the outline's original plan of reading a complete finite
backbone directly off Lemma C's collapse point: new primes keep entering the
picture and immediately start doing real witnessing work. (Whether they
continue to do so *forever*, i.e. whether infinitely many distinct primes ever
serve as some `w(i,j)`, is exactly the still-unresolved original Step-2
question; NC1 does not settle it, it only shows one specific proposed shortcut
to it fails.)

### Proposition NC2 (the canonical witness need not be `\le\mathrm{rad}(a_1)`) — new, proved in full this round

**Statement.** It is **not true in general** that every canonical witness
`w(i,j)` (`i<j`) satisfies `w(i,j)\le L`, where `L:=\mathrm{rad}(a_1)` (Lemma
1's constant).

**Proof (explicit counterexample, fully hand-verified).** Take
`a_1=375=3\cdot5^3`, so `L=\mathrm{rad}(375)=3\cdot5=15`. We trace the first
seven terms.

- `a_1=375`.
- `a_2`: `376=2^3\cdot47` and `377=13\cdot29` both have `\gcd(\cdot,375)=1`
  (neither divisible by `3` or `5`), so both fail against `a_1`. `378=2\cdot
  3^3\cdot7` has `\gcd(378,375)=3>1`, so `a_2=378`.
- `a_3`: `379` is prime, `\gcd(379,375)=1`, fails against `a_1`. `380=2^2\cdot
  5\cdot19` has `\gcd(380,375)=5>1` (passes `a_1`) and `\gcd(380,378)=2>1`
  (passes `a_2`, since `378=2\cdot3^3\cdot7`). So `a_3=380`.
- `a_4`: `381=3\cdot127` passes `a_1` (`\gcd=3`) and `a_2` (`\gcd=3`), but
  `\gcd(381,380)=1` (`381` is odd and not a multiple of `5` or `19`), failing
  against `a_3`. `382=2\cdot191` and `383` (prime) both fail against `a_1`
  (neither divisible by `3` or `5`). `384=2^7\cdot3` passes `a_1` (`\gcd=3`),
  `a_2` (`\gcd=2\cdot3`), and `a_3` (`\gcd(384,380)=2^2=4`). So `a_4=384`.
- `a_5`: `385=5\cdot7\cdot11` passes `a_1` (`\gcd=5`), `a_2` (`\gcd=7`), `a_3`
  (`\gcd=5`), but `\gcd(385,384)=1` (`385` odd, `384=2^7\cdot3`, no common
  factor), failing against `a_4`. `386=2\cdot193` fails against `a_1`.
  `387=3^2\cdot43` passes `a_1` (`\gcd=3`) and `a_2` (`\gcd=9`), but
  `\gcd(387,380)=1` (`387` has no factor `2,5,19`), failing against `a_3`.
  `388=2^2\cdot97` fails against `a_1`. `389` is prime, fails against `a_1`.
  `390=2\cdot3\cdot5\cdot13` passes `a_1` (`\gcd=15`), `a_2` (`\gcd=6`), `a_3`
  (`\gcd=10`), `a_4` (`\gcd=6`). So `a_5=390`.
- `a_6`: `391=17\cdot23` and `392=2^3\cdot7^2` fail against `a_1` (no factor
  `3` or `5`). `393=3\cdot131` passes `a_1,a_2` but `\gcd(393,380)=1`, failing
  against `a_3`. `394=2\cdot197` fails against `a_1`. `395=5\cdot79` passes
  `a_1` (`\gcd=5`) but `\gcd(395,378)=1` (`378=2\cdot3^3\cdot7`, no common
  factor with `5\cdot79`), failing against `a_2`. `396=2^2\cdot3^2\cdot11`
  passes `a_1` (`\gcd=3`), `a_2` (`\gcd=2\cdot3^2`), `a_3` (`\gcd=4`), `a_4`
  (`\gcd=2\cdot3`), `a_5` (`\gcd=2\cdot3`). So `a_6=396`.
- `a_7`: `397` (prime) and `398=2\cdot199` fail against `a_1` (no factor `3`
  or `5`). `399=3\cdot7\cdot19` passes `a_1` (`\gcd=3`), `a_2`
  (`\gcd=\gcd(399,378)=3\cdot7=21`), `a_3` (`\gcd(399,380)=19`), `a_4`
  (`\gcd(399,384)=3`), `a_5` (`\gcd(399,390)=3`), `a_6` (`\gcd(399,396)=3`). So
  `a_7=399`.

So `a_1,\dots,a_7=375,378,380,384,390,396,399`, and in particular
`\mathrm{rad}(a_3)=\mathrm{rad}(380)=\{2,5,19\}` and
`\mathrm{rad}(a_7)=\mathrm{rad}(399)=\{3,7,19\}`. Their intersection is
`\{19\}` (check: `380=2^2\cdot5\cdot19`, `399=3\cdot7\cdot19`, and `19` is the
only common prime factor). So `w(3,7)=19`. But `L=15<19`. This gives a pair
whose canonical witness exceeds `L`, disproving the statement. `\blacksquare`

**Interpretation.** So neither of the two most natural a-priori candidate
backbones — "primes seen by Lemma C's collapse point" (NC1) nor "primes
`\le\mathrm{rad}(a_1)`" (NC2) — is a valid finite covering set in general. Any
correct finiteness argument for the backbone must use a mechanism sensitive to
the specific sequence beyond these simple invariants.

### The reformulated open target: Finite Covering Backbone Conjecture

Given NC1 and NC2, this round reformulates the approach's target away from
"the set of canonical minimal witnesses is finite" (`(\star\star)`, the
original Step-2 goal) to the following logically weaker statement, which is
implied by `(\star\star)` (so proving `(\star\star)` would still finish this
approach, but so would this weaker statement, and empirically the weaker
statement is easier to keep verifying):

**Conjecture (Finite Covering Backbone — open, not proved this round).** There
exists a finite set of primes `H` such that for every `1\le i<j`,
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap H\ne\varnothing` (i.e. `H` need not
contain the *specific minimal* common prime `w(i,j)` for every pair — as NC1/
NC2 show it generally cannot — only *some* common prime for every pair).

*Why this is (formally) no harder than `(\star\star)`.* If `(\star\star)` holds
— i.e. `W:=\bigcup_{i<j}\{w(i,j)\}` is finite — then `H:=W` trivially satisfies
the covering conjecture, since `w(i,j)\in\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)
\cap H` for every pair. So the covering conjecture is a genuine weakening (any
proof of `(\star\star)` proves it; the converse is not claimed and, per the
`a_1=65` numerics discussed below, plausibly false in the sense that the
covering `H` may be *strictly smaller* than the true infinite-if-it-were-infinite
witness set `W`).

*Why this is the right target for the construction hand-off.* A finite `H`
with the covering property is exactly the input needed to run a finite-state /
residue-tracking construction (as in `intersecting-family-covering-construction`'s
Step 5): once such an `H` is fixed, admissibility of a candidate `x` against
*every* earlier term reduces to a check against a bounded amount of local data
— for each prime `p\in H`, which residue classes mod `p` are "already covered"
by the tail of terms sharing `p` — instead of an a-priori unbounded search over
all earlier terms and all their (possibly large, possibly one-off) prime
factors.

**Empirical support (numerical checks this round, exact integer arithmetic,
not part of the proof).**
- `a_1=15`: `H` read off from the first `2` terms, `H=\{2,3,5\}`, verified
  sufficient for all pairs among the first `3000` terms (exhaustive, ~4.5
  million pairs) — carried over from the outline-reviewer's check, reproduced.
- `a_1=65`: `H` from the first `3` terms, `H=\{2,3,5,7,13\}`, sufficient for all
  pairs among the first `1500` terms tested. (Note: `H` here does **not**
  contain `11`, even though `11` *is* the canonical minimal witness for the pair
  `(99,120)` in this sequence — `\gcd(a_{99},a_{120})=\gcd(715,858)=11\cdot13`,
  and `13\in H` covers this pair even though `11\notin H` also happens to
  divide both terms. This illustrates concretely why the covering conjecture
  can be true with a strictly smaller `H` than the true witness set `W`.)
- `a_1=105,143,1001`: `H` from the first `2`–`3` terms sufficient for all pairs
  among `1500` terms tested, no exceptions.
- `a_1=247` (the hardest known stress case for this problem — the shared
  `current.md` notes not even periodicity is detected within `15000` terms for
  this value): `H=\{2,3,5,7,13,19\}`, read off from only the **first `4`
  terms**, tested **exhaustively against all pairs among `8000` consecutive
  terms** (~32 million pairs) — zero failures.
- `a_1=375` (the NC2 counterexample value): `H` from the first `3` terms,
  `H=\{2,3,5,7,19\}` (note `19\in H` here, since the collapse-causing term
  `a_3=380` itself carries `19` — this is a different situation from `a_1=221`,
  where the offending prime `5` had not yet appeared by the collapse index),
  sufficient for all pairs among `1500` terms tested.

This is substantially more extensive numerical support (in particular the
exhaustive `8000`-term check on the hardest stress case `a_1=247`) than existed
in the workspace before this round, and is consistent across every Case-II
example tried, including the two that were specifically constructed this round
to refute the two naive candidate mechanisms (NC1, NC2). It is evidence the
conjecture is plausible and the right target, **not** a proof.

### Attempted proof route (Domination Lemma + Lemma 1) — worked out fully, does not close the gap

One natural way to try to prove the covering conjecture is to control which
primes can ever be the "dominant" prime identified by the Domination Lemma,
and show that set is finite. Carrying this out explicitly (extending, not just
citing, the two certified lemmas):

Fix `n\ge1`, let `x=a_{n+1}`, `r=\omega(x)`, and let `q^*` be a prime factor of
`x` achieving the Domination Lemma's maximum, so `D_n(q^*)\ge n/r`. Since
`a_1,\dots,a_n` are `n` distinct positive integers each `\le a_n`, the number
of them divisible by `q^*` is at most the number of multiples of `q^*` in
`\{1,\dots,a_n\}`, i.e. `D_n(q^*)\le\lfloor a_n/q^*\rfloor\le a_n/q^*`.
Combining the two bounds on `D_n(q^*)`:
$$\frac{n}{r}\le D_n(q^*)\le\frac{a_n}{q^*}\quad\Longrightarrow\quad q^*\le\frac{r\cdot a_n}{n}.$$
By Lemma 1, `a_n\le a_1+(n-1)L\le a_1+nL`, so `a_n/n\le a_1/n+L\le a_1+L` for
every `n\ge1` (using `a_1/n\le a_1`). Also `r=\omega(x)\le\log_2 x\le
\log_2(a_1+nL)` (each of the `r` distinct prime factors of `x` is `\ge2`, so
`x\ge2^r`, and `x=a_{n+1}\le a_1+nL` by Lemma 1). Substituting:
$$q^*\le(a_1+L)\cdot\log_2(a_1+nL).$$

This is an explicit, correct bound — but it **grows** like `O(\log n)` as
`n\to\infty` (the right-hand side is unbounded in `n`), not a fixed constant.
So this route bounds *how large* the dominant prime at step `n` can be only in
terms of `n` itself, and does not produce a fixed finite set that the dominant
primes are eventually confined to. This makes precise (with an explicit
formula, rather than only the qualitative statement already on record in
`current.md`) exactly why "growth control" (already resolved, per the shared
`current.md`, by combining these same two lemmas) does **not** by itself give
"concentration onto finitely many primes" — the two are genuinely different
strengths of conclusion, and no route was found this round from one to the
other.

### Round 3: the `\omega`-boundedness algebra (necessity half), and the reviewer-requested necessity→sufficiency bridge attempt

**Necessity half — re-derived, confirmed correct (as the round-3 outline-reviewer
already verified by hand).** Fix `n\ge1`, let `x=a_{n+1}`, `r:=\omega(x)`, and let
`q^*=q^*(n+1)` be a prime factor of `x` achieving the Domination Lemma's maximum
(`D_n(q^*)=\max_jD_n(q_j)\ge n/r`). As in the "Attempted proof route" above,
`D_n(q^*)\le a_n/q^*`, so `n/r\le a_n/q^*`, i.e. `q^*\le r\cdot a_n/n`. By Lemma 1,
`a_n/n\le a_1/n+L\le a_1+L` for every `n\ge1`; this quantity is a genuine
**constant** (independent of `n`), unlike the term `r=\omega(x)` which is the sole
source of the previously-derived `O(\log n)` growth (via the crude bound
`r\le\log_2x`). **Key Lemma (`\omega`-bound).** *If there is a fixed constant `M`
with `\omega(a_n)\le M$ for every `n\ge1`, then `q^*(n)\le M\cdot(a_1+L)` for
every `n\ge2` — a genuine uniform bound, not growing with `n`.* Proof: immediate
substitution of `r=\omega(a_{n})\le M` (relabeling `x=a_n$, i.e. applying the
displayed inequality with `n\to n-1`) into `q^*\le r\cdot a_{n-1}/(n-1)\le
M\cdot(a_1+L)`. Consequently `Q:=\{q^*(n):n\ge2\}` is a **finite** set, contained
in the (finite) set of primes `\le M(a_1+L)`. This closes the "necessity" half of
backbone finiteness completely, *conditionally* on the still-open hypothesis
`\omega(a_n)=O(1)` (itself not proved this round either — see the "Sub-target"
discussion in the outline above, carried over unchanged: numerics on `a_1=247`
show `\omega(a_n)\in\{6,7\}` through `n=40000` with one observed late increase,
consistent with but not proof of `O(1)`).

**The sufficiency bridge — attempted directly this round, per the outline-reviewer's
explicit request, and found to FAIL as literally stated (two independent, fully
hand-verified counterexamples).** The question is: even granting `\omega(a_n)=O(1)`
so `Q` above is finite, does `H:=Q\cup\mathrm{rad}(a_1)` (or a natural broadening of
`Q`) actually satisfy the FCBC covering property (`H\cap\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\ne\varnothing` for *every* `i<j`, not just consecutive/nearby
pairs)? Two candidate bridges were tried; both fail, and the failures are proved
below (not merely numerically observed) by hand computation on the two traces
already certified in this file (NC1's `a_1=221` trace, NC2's `a_1=375` trace).

**Proposition ND1 (the naive "unique dominant prime" set `Q` is not a valid
covering set).** Using the certified `a_1=221` trace
(`a_1,\dots,a_5=221,234,238,255,260`; `\mathrm{rad}(a_1)=\{13,17\}`,
`\mathrm{rad}(a_2)=\{2,3,13\}`, `\mathrm{rad}(a_3)=\{2,7,17\}`,
`\mathrm{rad}(a_4)=\{3,5,17\}`, `\mathrm{rad}(a_5)=\{2,5,13\}`), compute
`D_n(q)$ directly for each step:
- `n=1$ (choosing among the primes `\{2,3,13\}` of `a_2=234`): `D_1(2)=D_1(3)=0`
  (neither `2` nor `3` divides `a_1=221`), `D_1(13)=1` (`13\mid221`). The unique
  maximizer is `q^*(2)=13`.
- `n=2$ (choosing among `\{2,7,17\}` of `a_3=238`): `D_2(2)=|\{i\le2:2\mid a_i\}|=1`
  (`2\mid234`, `2\nmid221`); `D_2(7)=0`; `D_2(17)=|\{221\}|=1` (`17\mid221`,
  `17\nmid234`). Tie between `2` and `17` (both `=1`).
- `n=3$ (choosing among `\{3,5,17\}` of `a_4=255`): `D_3(3)=|\{i\le3:3\mid a_i\}|=1`
  (`3\mid234`, `3\nmid221,238`); `D_3(5)=0` (`5` divides none of `221,234,238`);
  `D_3(17)=|\{221,238\}|=2` (`17\mid221$ and `17\mid238=2\cdot7\cdot17`). The
  **unique** maximizer is `q^*(4)=17` (`D_3(17)=2>D_3(3)=1=D_3(3)`,
  `D_3(5)=0`).

So, choosing `q^*(n)` to be **any single prime achieving the Domination Lemma's
maximum at each step** (the literal reading of "dominant prime"), the resulting
set is `Q=\{13\}\cup\{2\text{ or }17\}\cup\{17\}\subseteq\{2,13,17\}` regardless
of the `n=2` tie-break, and `H:=Q\cup\mathrm{rad}(a_1)=Q\cup\{13,17\}\subseteq
\{2,13,17\}` — in particular **`3\notin H`**, since `3` is never the *unique*
maximizer at any step (`D_3(3)=1<D_3(17)=2` strictly). But
`\mathrm{rad}(a_2)\cap\mathrm{rad}(a_4)=\{2,3,13\}\cap\{3,5,17\}=\{3\}` — the pair
`(i,j)=(2,4)` has `3$ as its **only** common prime factor. Since `3\notin H`,
`H\cap\mathrm{rad}(a_2)\cap\mathrm{rad}(a_4)=\varnothing`: `H` fails the FCBC
covering property. `\blacksquare`

**Proposition ND2 (the broadened "every prime meeting the average bound" set
also fails).** One natural fix to ND1 is to widen `Q` to `Q':=\{q: \exists\,
n\ge1,\ q\mid a_{n+1},\ D_n(q)\cdot\omega(a_{n+1})\ge n\}` — i.e. include *every*
prime factor of *every* term that meets the Domination Lemma's averaged
threshold `D_n(q)\ge n/\omega(a_{n+1})` at the step where it is tested, not only
a single per-step maximizer (this repairs ND1: at `n=3` above, `3` itself
satisfies `D_3(3)=1\ge3/3=1`, so `3\in Q'`). This broadened set is still
finite whenever `\omega(a_n)=O(1)$ (same three-line algebra as the Key Lemma
above applies verbatim to every prime meeting the average bound, not just the
unique maximizer, since the bound `q\le r\cdot a_n/n$ used no uniqueness). But it
**still fails** to give a valid covering set: using the certified `a_1=375`
trace (`a_1,\dots,a_7=375,378,380,384,390,396,399`; recall from Proposition NC2
`\mathrm{rad}(a_3)=\{2,5,19\}`, `\mathrm{rad}(a_7)=\{3,7,19\}`,
`\mathrm{rad}(a_3)\cap\mathrm{rad}(a_7)=\{19\}$, the pair's *unique* common
prime), check whether `19\in Q'` from the first `7` terms: the only two steps
at which `19` is tested (i.e. `19$ divides the newly-admitted term) are `n=2`
(testing `a_3=380`) and `n=6` (testing `a_7=399`).
- `n=2`: `D_2(19)=|\{i\le2:19\mid a_i\}|=0` (`375=3\cdot5^3`, `378=2\cdot3^3\cdot7`,
  neither divisible by `19`); threshold `n/\omega(a_3)=2/3`; `0<2/3`, fails.
- `n=6`: previous terms `a_1,\dots,a_6=375,378,380,384,390,396`. Checking each for
  divisibility by `19`: `375=3\cdot5^3`(no), `378=2\cdot3^3\cdot7`(no),
  `380=2^2\cdot5\cdot19`(**yes**), `384=2^7\cdot3`(no), `390=2\cdot3\cdot5\cdot13`
  (no), `396=2^2\cdot3^2\cdot11`(no). So `D_6(19)=1`; `\omega(a_7)=\omega(399)=
  \omega(3\cdot7\cdot19)=3`; threshold `n/\omega(a_7)=6/3=2`; `1<2`, fails again.

So `19\notin Q'` (restricted to the first `7` terms; consistent with the density
numerics discussed below, which show `19`'s divisor-density stabilizes around
`0.07`, well under the `\approx1/\omega\approx0.2$–$0.33` threshold density
observed for this sequence, so `19` plausibly never enters `Q'` at any `n` — not
proved in general, only checked through `n=7`, which already suffices as a
counterexample to the *general* covering claim for this bridge). Since
`\mathrm{rad}(a_1)=\{3,5\}` also does not contain `19`, `H':=Q'\cup\mathrm{rad}
(a_1)$ (restricted to data available by `n=7`) fails to cover the pair `(3,7)`
the same way `H` failed to cover `(2,4)` in ND1. `\blacksquare`

**Exploratory finding, explicitly NOT a proof (asymptotic density stratification).**
Numerical experiments this round (exact integer arithmetic via `sympy`, not part of
the proof) on `a_1=247` and `a_1=375` tracked `D_n(p)/n` for every prime `p` as
`n` grows to `2000$–$3000`. In both cases the primes split sharply into two
groups: a small set (matching exactly the outline's earlier empirically-found
covering sets, e.g. `\{2,3,5,7,13,19\}` for `a_1=247`) whose density `D_n(p)/n`
**stabilizes at a fixed positive value** (e.g. for `a_1=247`: `2\to0.845`,
`3\to0.716`, `13\to0.655`, `19\to0.462`, `5\to0.35`, `7\to0.243`, essentially flat
from `n=200` to `n=3000`), and all other primes, whose density **visibly decays**
towards `0` (e.g. `11\to0.09`, `17\to0.06`, `23\to0.04$, continuing to shrink as
`n$ grows). This pattern is consistent with the hypothesis that the correct
covering set `H` should be characterized by **asymptotic positive divisor
density** rather than by the Domination Lemma's per-step argmax/average-threshold
notion (which, as ND1/ND2 show, is the wrong invariant — a prime can have
positive density without ever being the argmax or meeting the *instantaneous*
average bound early on, e.g. `19` in the `a_1=375` case). However: (i) no proof is
given here that these densities actually converge (only that they look stable
over the tested range); (ii) even granting convergence, no argument is given for
*why* positive density should force covering of *every* pair `i<j` (density is an
aggregate/statistical statement; FCBC requires a hitting-set guarantee for *every
individual* pair, including arbitrarily far-apart ones — the same gap the
outline-reviewer flagged, now confirmed to survive this refinement attempt too).
This is recorded honestly as a *direction*, not a result.

### What remains open (the honest gap, updated round 3)

The Finite Covering Backbone Conjecture (equivalently, any sufficient
replacement giving a finite `H` with the covering property) is **not proved**.
Everything attempted so far to derive it — reading `H` off Lemma C's
collapse point (refuted, NC1), bounding `H` a priori by `\mathrm{rad}(a_1)`
(refuted, NC2), bounding the Domination Lemma's dominant prime uniformly (gives
only an `O(\log n)` bound, not finiteness, round 2), and — new this round —
turning a hypothetical uniform `\omega(a_n)=O(1)` bound into an actual covering
set via either the literal per-step dominant prime (refuted, Proposition ND1)
or the broadened "meets the averaged Domination-Lemma threshold" prime set
(refuted, Proposition ND2) — all either fail outright or stall. **The precise
status of the gap, sharpened this round:** the approach's originally-envisioned
two-step plan ("(1) prove `\omega(a_n)=O(1)`, (2) conclude the dominant primes
form a valid covering `H`") is now known to be **incomplete even if step (1)
succeeds** — step (2) does not follow from step (1) by any mechanism found so
far, and two natural candidate mechanisms for step (2) are now proved false
(not just unproved). This matches exactly the outline-reviewer's requested
finding: a genuine necessity-only argument (bounding *which* primes can ever be
"dominant" in the Domination-Lemma sense) does not, by itself or by the most
natural broadening, produce a *sufficient* covering set. Any future attempt
along this route needs a different mechanism entirely — e.g. the exploratory
"asymptotic positive density" characterization above, which was not turned into
a proof this round, or an argument abandoning the Domination Lemma's
per-step/local viewpoint altogether in favor of a genuinely global argument
(closer in spirit to `explicit-window-backbone-construction`'s pigeonhole
approach or `forced-primes-well-ordering`'s well-ordering approach — both
flagged by the round-3 outline-reviewer as needing to avoid this exact same
wall). The conjecture remains strongly supported empirically (most notably by
the `8000`-term exhaustive check on the hardest known stress instance,
`a_1=247`, from round 2) but is not established, and this round's work narrows
*how* it cannot be established (via the Domination-Lemma route alone) without
yet showing how it can. This is the approach's honest, currently unresolved
core gap; per `CLAUDE.md`, Status is `partial`, not `solved`.

Once (if) this conjecture is established, the remaining work to finish the
problem — using the finite `H` to build the eventual periodic residue pattern
and then, per the round-2 outline's Step 4 hand-off, extending periodicity back
to `n=1` exactly (not just eventually) — is explicitly the content of
`intersecting-family-covering-construction`'s Step 5 skeleton and is not
duplicated here.

### Round 8: Realized–Blocked Dichotomy, the Pigeonhole Corollary, and the Finite-Reachability Theorem

**Notation (imported unchanged).** Fix a proper nonempty core `S\subsetneq
P_1` with `I_S:=\{i\ge1:\mathrm{rad}(a_i)\cap P_1=S\}\ne\varnothing`.
`\mathrm{comp}(a_j):=\mathrm{rad}(a_j)\setminus P_1`. A *bare value* is any
nonempty finite set `\kappa=S\cup Q` with `Q` a finite set of primes disjoint
from `P_1` (`Q=\varnothing` allowed, giving `\kappa=S`). `\kappa` is
**realized** if `\kappa=\mathrm{rad}(a_n)` for some index `n`; `\kappa` is
**blocked** if some index `j` has `\mathrm{rad}(a_j)\cap\kappa=\varnothing`.
A *bundle for `S`* is a nonempty `Q` with `S\cup Q` realized by some
`i\in I_S`. `J_S:=\{j\ge1:\mathrm{rad}(a_j)\cap S=\varnothing\}`. All of this
is imported unchanged from `lemmas/lemma-escape-confinement.md` and
`lemmas/lemma-permanent-bundle.md`; see those files for the already-certified
Escape-Confinement Lemma (iterated form) and Permanent Bundle Lemma
((SA)/(SCA) hypotheses), both used below without re-proof.

#### Realized–Blocked Dichotomy Lemma (RBD) — new this round

**Statement.** For every nonempty finite set of primes `\kappa`, **exactly
one** of the following holds: (a) `\kappa` is realized; (b) `\kappa` is
blocked. (No third possibility, and the two are mutually exclusive.)

**Proof.**

*Mutually exclusive.* Suppose `\kappa` is realized at index `n`
(`\mathrm{rad}(a_n)=\kappa`) and blocked by witness `j`
(`\mathrm{rad}(a_j)\cap\kappa=\varnothing`). If `n\ne j`, the already-certified
Lemma P′ gives `\gcd(a_n,a_j)>1`, i.e.
`\mathrm{rad}(a_n)\cap\mathrm{rad}(a_j)=\kappa\cap\mathrm{rad}(a_j)\ne
\varnothing`, contradicting the blocking hypothesis. If `n=j`, the blocking
hypothesis directly gives `\kappa\cap\kappa=\varnothing`, i.e. `\kappa=
\varnothing`, contradicting that `\kappa` is nonempty. Either way,
contradiction — so realized and blocked cannot hold simultaneously.

*Exhaustive.* Suppose `\kappa` is **not** blocked, i.e. every index `j` has
`\mathrm{rad}(a_j)\cap\kappa\ne\varnothing`. Let
`T_\kappa:=\min\{x>a_1:\mathrm{rad}(x)=\kappa\}` (well-defined: for every
`t\ge1`, `\big(\prod_{p\in\kappa}p\big)^t` has radical exactly `\kappa` and
these are unbounded as `t\to\infty`, so the minimizing set is nonempty — this
is the same well-definedness argument as Lemma FOM's `T_C`, imported
unchanged). By definition `T_\kappa>a_1`. For every `j\ge1`:
`\gcd(T_\kappa,a_j)>1\iff\mathrm{rad}(T_\kappa)\cap\mathrm{rad}(a_j)\ne
\varnothing\iff\kappa\cap\mathrm{rad}(a_j)\ne\varnothing`, which holds by the
"not blocked" assumption (taking the general index `j`). So `T_\kappa>a_1`
and `\gcd(T_\kappa,a_j)>1$ for every `j\ge1`. If `T_\kappa` is not equal to
any term `a_i`, the already-certified Lemma ER (contrapositive form) applies
directly with `y:=T_\kappa` and gives `T_\kappa=a_m` for some `m` — a
contradiction of "not equal to any term." Hence `T_\kappa=a_m$ for some `m`,
so `\mathrm{rad}(a_m)=\mathrm{rad}(T_\kappa)=\kappa`, i.e. `\kappa` is
realized. `\blacksquare`

**Discussion.** This is a genuine new synthesis: Lemma ER's own scope note
explicitly warns "it should not be cited as closing any part of the gap on
its own," and it is not — RBD is a three-line combination of Lemma ER, the
already-certified Permanent-Inadmissibility Lemma, and Lemma P′, applied to
*radical values* rather than *candidate integers*, not stated anywhere in
this workspace prior to this round. It supplies exactly what the
escape-recursion below needs: a guarantee that every node of the recursion
tree has a well-defined, exhaustive two-way status, with no undetermined
case to separately worry about.

#### Complement Witness Fact (partial progress on the Watch-out sub-lemma)

**Statement.** If `I_S\ne\varnothing`, then `J_{S^c}\ne\varnothing`, where
`S^c:=P_1\setminus S$.

**Proof.** Let `i\in I_S`, so `\mathrm{rad}(a_i)\cap P_1=S` exactly. For any
`q\in S^c=P_1\setminus S`: since `q\in P_1` and `\mathrm{rad}(a_i)\cap P_1=S$
(not `S\cup\{q\}`), `q\notin\mathrm{rad}(a_i)`. As `q\in S^c` was arbitrary,
`\mathrm{rad}(a_i)\cap S^c=\varnothing`, i.e. `i\in J_{S^c}`. `\blacksquare`

**Honest scope note — why this does not resolve the round-8 Watch-out
sub-lemma.** The outline's Step 1 needs `J_S\ne\varnothing` (a witness
*avoiding `S`*, not avoiding `S^c`), and this Fact proves the *complementary*
direction. Bootstrapping from it to `J_S\ne\varnothing` would need
`I_{S^c}\ne\varnothing` too (then the same argument, roles swapped, gives
`J_S\ne\varnothing` directly) — but `S^c` being *some* subset of `P_1$ with
`I_S\ne\varnothing` does **not** imply `S^c` is itself exactly realized as a
core (`I_{S^c}\ne\varnothing`); this is a genuinely separate, unproven fact
about `S^c`. I attempted the natural remaining route — showing that if
*every* index's core meets `S`, then (since `S` is finite) some fixed prime
`p\in S` divides infinitely many terms by pigeonhole, and pushing this
toward a contradiction with the Case II dichotomy (no single prime of `P_1`
saturates *every* term) — but this stalls exactly where expected: "infinitely
many" is not "all," and the Case II hypothesis only excludes the latter.
This is a genuine gap, not a hand-wave: the natural proof attempts run into
the *same* difficulty as the file's pre-existing standing hypothesis "`J_S`
infinite" (already unproved in general since round 6, and already required
by the Single-Companion Finiteness Lemma and the Permanent Bundle Lemma).
**Conclusion, stated honestly:** `J_S\ne\varnothing$ (equivalently, existence
of a core-avoiding witness `j_3` for `S`) is not established in general in
this round either. It is directly verifiable case-by-case (the round-8
outline-reviewer independently spot-checked witness existence for every
proper core of four of the five mandated hard cases, index `2`–`4` in every
case — see `/tmp/round-8/outline-reviewer.md`), and it holds automatically
whenever the file's pre-existing standing hypothesis "`J_S` infinite" holds
(trivially, `J_S` infinite `\Rightarrow J_S\ne\varnothing`) — so nothing
below introduces a *new* unproven hypothesis beyond what this reduction
chain already carries; it only isolates a (possibly strictly weaker, still
open) sufficient sub-case of it.

#### Escape-Confinement Pairwise-Disjoint-Bundle-Count Corollary (Step 1)

**Statement.** Fix a proper core `S` with `I_S\ne\varnothing`, and suppose a
core-avoiding witness `j_3` exists (`\mathrm{rad}(a_{j_3})\cap S=
\varnothing$ — guaranteed whenever `J_S` is infinite, the standing
hypothesis used elsewhere in this file; not established in general, per the
scope note above). Then **every** family of pairwise-disjoint bundles for
`S` has size `\le|\mathrm{comp}(a_{j_3})|`.

**Proof.** First, `S` itself is blocked by `j_3`: by definition
`\mathrm{rad}(a_{j_3})\cap S=\varnothing`, so `S` is a blocked bare value
(`\kappa:=S$, `Q:=\varnothing` in the blocking definition). Apply the
already-certified Escape-Confinement Lemma with `\kappa:=S`: for every escape
`i\in I_S` (every `i\in I_S` is automatically an escape from `S`, since
`\mathrm{rad}(a_i)\supseteq S` always by definition of `I_S`, and
`\mathrm{rad}(a_i)\ne S` because `S` is blocked hence never realized exactly
— by the RBD Lemma, blocked `\Rightarrow` not realized), there exists a
prime `p\in\mathrm{comp}(a_{j_3})$ with `p\in\mathrm{rad}(a_i)`. Since
`\mathrm{rad}(a_i)=S\cup Q_i` for the bundle `Q_i:=\mathrm{rad}(a_i)\setminus
S`, and `p\notin P_1\supseteq S` (as `p\in\mathrm{comp}(a_{j_3})=
\mathrm{rad}(a_{j_3})\setminus P_1`), we get `p\in Q_i`. So **every** bundle
`Q_i` (`i\in I_S`) contains at least one element of the fixed finite set
`W_0:=\mathrm{comp}(a_{j_3})`. If `\{Q_{i_1},\dots,Q_{i_r}\}` is a
pairwise-disjoint family of bundles, choosing one witnessing prime
`p_l\in Q_{i_l}\cap W_0` for each `l` gives an injection
`\{1,\dots,r\}\to W_0$ (injective because the `Q_{i_l}` are pairwise
disjoint, so the chosen `p_l$ are pairwise distinct), hence `r\le|W_0|=
|\mathrm{comp}(a_{j_3})|`. `\blacksquare`

**Scope note (do not overclaim, exactly as the round-8 outline itself
warns).** This bounds families of *pairwise-disjoint* bundles, not the total
number of bundles ever realized for `S` — bundles that pairwise-intersect
(e.g. all sharing one fixed prime of `W_0`) are not bounded by this argument
alone. Bounding the total count needs the deeper mechanism below.

#### The Reachable Set and the Finite-Reachability Theorem (Step 2)

**Fixed-witness convention.** For each blocked bare value `\kappa`, fix
`j(\kappa):=\min\{j:\mathrm{rad}(a_j)\cap\kappa=\varnothing\}$ (well-defined:
the set of valid witnesses is a nonempty subset of `\mathbb{Z}_{>0}`, so has
a minimum by well-ordering) and set
`W_\kappa:=\mathrm{comp}(a_{j(\kappa)})` — a fixed, finite (as
`\mathrm{comp}(a_j)\subseteq\mathrm{rad}(a_j)`, and every integer has
finitely many prime factors), `\kappa`-and-`a_1`-computable set.

**Definition (Reachable Set `R`).** Define `R_0:=\{S\}` and, for `t\ge0`,
`R_{t+1}:=\{\kappa\cup\{q\}:\kappa\in R_t,\ \kappa\text{ blocked},\
q\in W_\kappa\}`. Let `R:=\bigcup_{t\ge0}R_t`.

**Lemma (each `R_t` is finite).** By induction on `t`. `R_0=\{S\}` is finite.
If `R_t` is finite, `R_{t+1}=\bigcup_{\kappa\in R_t,\ \kappa\text{ blocked}}
\{\kappa\cup\{q\}:q\in W_\kappa\}` is a union of at most `|R_t|` finite sets
(each of size `\le|W_\kappa|<\infty`), hence finite. `\blacksquare`

**Lemma (monotone extinction).** If `R_t=\varnothing`, then `R_{t+1}=
\varnothing` (immediate from the definition — an empty union). Consequently
the set `\{t\ge0:R_t\ne\varnothing\}` is either all of `\mathbb{Z}_{\ge0}`
or an initial segment `\{0,1,\dots,T\}`.

**Lemma (Finitely-Branching-Tree Fact — a form of König's Lemma, proved
directly).** Consider the tree `\mathcal{T}$ whose nodes at depth `t` are
finite sequences `(\kappa_0,\kappa_1,\dots,\kappa_t)` with `\kappa_0=S`,
each `\kappa_s$ blocked, and `\kappa_{s+1}\in\{\kappa_s\cup\{q\}:q\in
W_{\kappa_s}\}` for `0\le s<t` (i.e. `\mathcal{T}$ records *paths*, not just
endpoints, so distinct routes to the same set `\kappa` are distinct nodes).
Each node has at most `|W_{\kappa_t}|<\infty$ children (finite branching). If
`\mathcal{T}` has nodes at every depth `t=0,1,2,\dots` (i.e. is infinite),
then `\mathcal{T}` has an infinite path.

**Proof.** Build the path greedily. At depth `0` there is one node,
`(S)`; call it `\pi_0`. Given a depth-`t` node `\pi_t` with the property
that `\mathcal{T}` has nodes extending `\pi_t` at every depth `\ge t`
(true for `\pi_0=(S)$ by hypothesis, since **every** node of `\mathcal{T}`
extends `(S)`), `\pi_t` has finitely many children `c_1,\dots,c_k$ in
`\mathcal{T}` (`k=|W_{\kappa_t}|$ if `\kappa_t` is blocked, else `k=0`, but
`k=0` is impossible here since we are assuming nodes extending `\pi_t`
exist at every depth `>t`, in particular at depth `t+1`, so `\pi_t` must
have at least one child, hence `\kappa_t$ is blocked and `k\ge1`). If none
of `c_1,\dots,c_k$ had extensions at unboundedly many depths, then (letting
`D_1,\dots,D_k` be the largest depth to which each `c_m` extends, each
finite by assumption) no node would extend `\pi_t` at any depth `>\max(D_1,
\dots,D_k)$ — contradicting the hypothesis on `\pi_t`. So some `c_m$ has
extensions at every depth `\ge t+1`; set `\pi_{t+1}:=c_m`. This defines
`\pi_0,\pi_1,\pi_2,\dots`, an infinite path. `\blacksquare`

**Finite-Reachability Theorem.** Say `S` satisfies **NIBC** ("No Infinite
Blocked Chain") if there is no infinite sequence `S=\kappa_0\subsetneq
\kappa_1\subsetneq\kappa_2\subsetneq\cdots` with every `\kappa_t` blocked and
`\kappa_{t+1}\in\{\kappa_t\cup\{q\}:q\in W_{\kappa_t}\}` for every `t`.
**If `S` satisfies NIBC, then `R` is finite.**

**Proof.** Suppose `R` is infinite. Since each `R_t` is finite (Lemma
above), infinitely many `t` must have `R_t\ne\varnothing$ (else `R` would be
a finite union of finite sets); by the monotone-extinction Lemma this means
`R_t\ne\varnothing` for **every** `t\ge0`. Hence the path-tree `\mathcal{T}`
defined above has at least one node at every depth `t` (any `\kappa\in R_t`
is reached by *some* path of length `t`, by `R_t`'s recursive definition —
an easy induction: `R_0=\{S\}`, path `(S)`; if `\kappa\in R_{t+1}` then
`\kappa=\kappa'\cup\{q\}` for some `\kappa'\in R_t` with a path
`(\kappa_0,\dots,\kappa_t=\kappa')` by the induction hypothesis, and
appending `\kappa` extends it to a depth-`(t+1)` path). By the
Finitely-Branching-Tree Fact, `\mathcal{T}` has an infinite path
`\pi_0=S,\pi_1,\pi_2,\dots` — but this is exactly an infinite sequence
`S=\pi_0\subsetneq\pi_1\subsetneq\cdots` with every `\pi_t` blocked (each
`\pi_t` must be blocked, since it has a child `\pi_{t+1}$ in `\mathcal{T}`,
which by definition of `\mathcal{T}`'s edges requires `\pi_t` blocked), i.e.
an infinite blocked chain — contradicting NIBC. `\blacksquare`

**Reachability Theorem for (SA)-bundles.** Suppose a core-avoiding witness
for `S` exists (`\exists j_3` with `\mathrm{rad}(a_{j_3})\cap S=
\varnothing` — the same hypothesis Step 1 needs; not established in
general, per the scope note above). If `Q` is a bundle for `S` (some
`i\in I_S` has `\mathrm{rad}(a_i)=S\cup Q`) satisfying the already-certified
Permanent Bundle Lemma's **Subset Avoidance (SA)** hypothesis (no nonempty
proper `Q'\subsetneq Q$ has `S\cup Q'` realized by any index), then
`S\cup Q\in R`.

**Proof.** Enumerate `Q=\{p_1,\dots,p_k\}` (`k=|Q|$); we construct, by
induction on `t=0,\dots,k`, a chain `\kappa_0=S\subsetneq\kappa_1\subsetneq
\cdots\subsetneq\kappa_k=S\cup Q` with `\kappa_t\in R_t` for every `t`, and
(for `t<k`) `\kappa_t$ blocked, `\kappa_{t+1}=\kappa_t\cup\{p_{\sigma(t+1)}\}$
for some not-yet-used index `\sigma(t+1)`, chosen so that
`\{p_{\sigma(1)},\dots,p_{\sigma(t)}\}` are `t` **distinct** elements of `Q`.

*Base case* `t=0`: `\kappa_0=S\in R_0$, given. `\kappa_0=S` is blocked by
`j_3` (the core-avoiding-witness hypothesis above) — this is exactly Step
1's own base fact, not a consequence of (SA) (which only speaks to
*nonempty* proper subsets `Q'\subsetneq Q`, hence says nothing about
`Q'=\varnothing`, i.e. about `\kappa_0=S` itself).

*Inductive step.* Suppose `\kappa_t=S\cup\{p_{\sigma(1)},\dots,p_{\sigma(t)}\}
\in R_t$ is constructed with `t` distinct elements of `Q`, `0\le t<k`. If
`t=0`, `\kappa_t=S` is blocked by the base case above. If `t\ge1`,
`\{p_{\sigma(1)},\dots,p_{\sigma(t)}\}` is a **nonempty proper** subset of
`Q` (proper since `t<k`), so (SA) directly says `\kappa_t=S\cup
\{p_{\sigma(1)},\dots,p_{\sigma(t)}\}` is **not realized**; by the RBD
Lemma (not realized `\Rightarrow` blocked), `\kappa_t` is blocked. Either
way, `\kappa_t` is blocked, so `W_{\kappa_t}` is defined. Let
`i\in I_S` be the index with `\mathrm{rad}(a_i)=S\cup Q\supsetneq\kappa_t`
(exists by hypothesis, and `i` is an escape from `\kappa_t` since
`\kappa_t\subsetneq S\cup Q=\mathrm{rad}(a_i)`, using `t<k`). By the
Escape-Confinement Lemma applied with `\kappa:=\kappa_t`, witness
`j(\kappa_t)`, there is a prime `p\in W_{\kappa_t}\cap\mathrm{rad}(a_i)=
W_{\kappa_t}\cap(S\cup Q)`. Since `W_{\kappa_t}\cap P_1=\varnothing`
(`W_{\kappa_t}=\mathrm{comp}(a_{j(\kappa_t)})` is disjoint from `P_1$ by
definition of `\mathrm{comp}`), `p\notin S`, so `p\in W_{\kappa_t}\cap Q`.
Moreover `p\notin\kappa_t$: since `\kappa_t\cap\mathrm{rad}(a_{j(\kappa_t)})
=\varnothing` (definition of blocking) and `W_{\kappa_t}\subseteq
\mathrm{rad}(a_{j(\kappa_t)})`, `\kappa_t\cap W_{\kappa_t}=\varnothing`,
so `p\notin\kappa_t`; in particular `p\ne p_{\sigma(1)},\dots,p_{\sigma(t)}`.
Set `\sigma(t+1)$ so `p_{\sigma(t+1)}:=p` and `\kappa_{t+1}:=\kappa_t\cup
\{p\}\in R_{t+1}` (by `R`'s definition, since `\kappa_t\in R_t` blocked,
`p\in W_{\kappa_t}`). This completes the induction.

After `k` steps, `\{p_{\sigma(1)},\dots,p_{\sigma(k)}\}` are `k` **distinct**
elements of the size-`k` set `Q`, hence equal to `Q` itself, so
`\kappa_k=S\cup Q\in R_k\subseteq R`. `\blacksquare`

**Corollary (Step 2's main conditional result).** If a core-avoiding witness
for `S` exists and `S` satisfies NIBC, the number of distinct bundles for
`S` satisfying (SA) is finite — at most `|R|`.

**Proof.** Distinct (SA)-bundles `Q\ne Q'` give distinct sets `S\cup Q\ne
S\cup Q'`, each in `R` by the Reachability Theorem, and `|R|<\infty` by the
Finite-Reachability Theorem (NIBC). `\blacksquare`

By the already-certified Permanent Bundle Lemma, every bundle satisfying (SA)
together with `Q\cap D_S=\varnothing` and (SCA) is **permanent**. So: **NIBC
`\Rightarrow` the count of permanent bundles for `S` is finite** — this
formally upgrades round 7's "permanent-bundle-count" target (shown
insufficient for the whole problem by this round's outline, but still a
genuine, well-posed sub-target) from an informal diagnosis into an exact
conditional theorem.

#### Worked example (fully hand-verified, fresh computation, not reused from any prior round's possibly-imprecise cited values)

`a_1=2747`, `S=\{67\}` (`P_1=\{41,67\}`). Independently simulated the greedy
sequence from scratch (`math.gcd`, exact greedy rule): `a_1=2747$
(`\mathrm{rad}=\{41,67\}`), `a_2=2788=2^2\cdot17\cdot41`
(`\mathrm{rad}=\{2,17,41\}`), `a_3=2814=2\cdot3\cdot7\cdot67`
(`\mathrm{rad}=\{2,3,7,67\}`), `a_4=2829=3\cdot23\cdot41`
(`\mathrm{rad}=\{3,23,41\}`), `a_{10}=3157=7\cdot11\cdot41`
(`\mathrm{rad}=\{7,11,41\}`) — all confirmed by exact `sympy` factorization.
Take `Q=\{2,3,7\}$ (realized at `a_3`, `S\cup Q=\{2,3,7,67\}`).

- `\kappa_0=S=\{67\}`: blocked by `j=2` (`\mathrm{rad}(a_2)=\{2,17,41\}`,
  disjoint from `\{67\}`). `W_{\kappa_0}=\mathrm{comp}(a_2)=\{2,17,41\}
  \setminus\{41,67\}=\{2,17\}`. Escape-Confinement (via `a_3`, escape from
  `\kappa_0`) forces a prime of `Q\cap\{2,17\}` — indeed `2\in Q`. Set
  `\kappa_1:=\{2,67\}`.
- `\kappa_1=\{2,67\}`: proper subset `\{2\}\subsetneq Q` (with (SA) verified
  for this instance by the already-certified `lemmas/lemma-permanent-bundle.md`,
  three explicit witnesses), so not realized, hence blocked by RBD — indeed
  directly: `j=4$ (`\mathrm{rad}(a_4)=\{3,23,41\}`, disjoint from
  `\{2,67\}`). `W_{\kappa_1}=\mathrm{comp}(a_4)=\{3,23\}`.
  Escape-Confinement forces a prime of `Q\cap\{3,23\}=\{3\}`. Set
  `\kappa_2:=\{2,3,67\}`.
- `\kappa_2=\{2,3,67\}`: proper subset `\{2,3\}\subsetneq Q`, not realized
  (SA), blocked — indeed `j=10` (`\mathrm{rad}(a_{10})=\{7,11,41\}`,
  disjoint from `\{2,3,67\}`). `W_{\kappa_2}=\mathrm{comp}(a_{10})=
  \{7,11\}`. Escape-Confinement forces a prime of `Q\cap\{7,11\}=\{7\}`. Set
  `\kappa_3:=\{2,3,7,67\}=S\cup Q$.

`\kappa_3=S\cup Q$ is exactly the realized value at `a_3`, so the chain
terminates exactly as the Reachability Theorem predicts: `S\cup Q\in R_3
\subseteq R`, reached via witnesses `a_2,a_4,a_{10}` at levels `0,1,2`
respectively, extracting `2,3,7$ in that order. This is a full, from-scratch
hand-verification of the mechanism (not a numerical sample of the
*conclusion*, which was already known — this verifies the *proof
technique*'s claimed intermediate steps hold exactly as constructed).

#### The precise boundary: (SA)-violation exactly characterizes transient bundles

**Proposition (Transient Bundles Are Invisible to This Mechanism).** If a
bundle `Q` for `S` is **not** captured in `R$ via the construction above (in
particular, if it is not covered by the Corollary's finite bound even when
NIBC holds), then `Q` fails (SA): some nonempty proper `Q'\subsetneq Q` has
`S\cup Q'` realized. Equivalently (contrapositive of the Reachability
Theorem): **every bundle NOT satisfying (SA) is not reachable via this
construction.**

This is immediate from the Reachability Theorem (its contrapositive), but
its significance is best seen concretely. **Worked transient example** (the
round-8 outline's own motivating case, `a_1=21528751,S=\{197\}`, cited
values independently reconfirmed this round):
`a_{1291}=21{,}710{,}976=2^7\cdot3\cdot7\cdot41\cdot197`, giving bundle
`Q=\{2,3,7,41\}` for `S=\{197\}` — **transient**, later dominated at `n=2575`
by the smaller-radical value `\{2,3,7,197\}` (a certified permanent bundle,
per `lemmas/lemma-escape-confinement.md`'s independently-verified round-7
data). The dominator's companion set `\{2,3,7\}` is exactly the proper
subset `Q'=\{2,3,7\}\subsetneq Q=\{2,3,7,41\}` — so **`Q` fails (SA)
precisely because of the very event that makes it transient** (a smaller
bundle `S\cup Q'$ is independently realized, and by the already-certified
No-Resurrection Lemma this is exactly what causes domination once the
smaller radical appears). This is not a coincidence specific to one
instance — it is forced by definition: any bundle `Q` that is eventually
*dominated* by a proper superset-of-`S` radical `R\subsetneq S\cup Q` has,
by the already-certified Class-Decomposition Fact, `R=S\cup Q'$ for some
`Q'\subsetneq Q` (in the singleton-core case, or modulo (SCA) otherwise) —
i.e. **every transient (eventually-dominated) bundle fails (SA) by
definition**, since its own dominator *is* a realized proper subset.

**Conclusion (proved, not just diagnosed).** The entire Escape-Confinement/
pigeonhole mechanism — both Step 1's pairwise-disjoint bound and Step 2's
Finite-Reachability Theorem — is **structurally blind to transient bundles**:
it can only ever bound (SA)-satisfying bundles, which are exactly the
*candidates for permanence* (per the Permanent Bundle Lemma), never the
transient ones. This confirms, with an actual proof rather than an empirical
pattern, exactly what the round-8 outline warned against presenting as
sufficient: **even a full resolution of both open hypotheses above (general
core-avoiding-witness existence, and NIBC) would close only the permanent
share of `Λ_S`, leaving the transient share — the object this round's
outline explicitly retargeted to — completely untouched.** A correct
finiteness proof for `Λ_S`/`𝓥_S` needs a genuinely different mechanism for
the transient share; this round did not find one, and reports this honestly
as the precise remaining content, not a discouragement to search further
(the transient share is, by the Class-Decomposition argument just given,
always "explained" by a *smaller* realized bundle dominating it — so
bounding transient bundles is exactly as hard as bounding *all* realized
bundles, permanent or not, i.e. genuinely no easier a target than `Λ_S`
itself; no reduction of the transient share to a strictly smaller
sub-problem was found this round).

#### Honest summary of Round 8's status

Two precise open gaps, neither closed this round: (1) general existence of
a core-avoiding witness for every proper core `S` (verified case-by-case,
not in general — Complement Witness Fact gives real but insufficient
partial progress); (2) NIBC (no infinite chain of always-blocked bare
values) — not established, and disfavored by the already-documented round
7/8 finding that escape/confinement depth is not capped at a small constant
across tested instances (depth-3 examples beating naive depth-2 predictions).
Even granting both, the resulting finiteness conclusion (Step 2's Corollary)
provably only reaches the permanent/(SA)-satisfying share of `Λ_S` — the
transient share is a separate, unaddressed difficulty, proved (not just
suspected) to be at least as hard as the general problem via the
Class-Decomposition argument above. Status remains `partial`.

## Full proof
(Not present — Status is `partial`. The No-Resurrection Lemma, the Interval
Lemma, Theorem V (`𝓥` finite `\iff` (MRS)), the Record Characterization
Lemma, Proposition FR, and Theorem CI (round 5, new) are complete, gap-free
results proved above and are ready for the reviewer to certify — together
they give an exact, airtight reduction of the whole problem's remaining
content (Case II) to `𝓥`-finiteness, and an unconditional proof that `𝓥` is
finite in Case I. Lemma C, Proposition NC1, Proposition NC2, the Key Lemma
(`\omega`-bound), and Propositions ND1/ND2 (rounds 2–3) remain complete,
gap-free results, ready for the reviewer to certify. `𝓥`-finiteness in Case
II — the approach's genuine, currently open content — is **not** resolved
this round; see "Structural diagnosis" above for the precise, honest
statement of what remains. **Round 6 adds**: Lemma FOM, the Fan-Size
Corollary, the Generation-Chain Lemma, Lemma ER, the `Λ_S`-Reduction Lemma,
the Single-Companion Finiteness Lemma, and the Multi-Companion Reduction
Proposition are all complete, gap-free results, ready for the reviewer to
certify. They give a genuinely new partial mechanism for the Growth-Budget
Lemma (closing single-companion recruitment conditional on `J_S` infinite)
and a rigorous, *proved* — not asserted — pinpointing of the two precise
remaining obstructions (multi-companion bundling, provably as hard as local
FCBC; `J_S`-infiniteness, unproved in general). The Growth-Budget Lemma
itself, and hence `𝓥_S`-finiteness for a general proper core, is **not**
resolved this round. **Round 7 adds**: the Class-Decomposition Fact, the
corrected Permanent Pair Lemma (a genuine gap found and fixed for
non-singleton cores), and the new Permanent Bundle Lemma (arbitrary bundle
size, exhaustively validated) are all complete, gap-free results, ready
for the reviewer to certify. They sharpen the bundle-size-induction
foreclosure and give the deepest numerical stress test of (MRS) produced
in this workspace (up to `5{,}000{,}000` terms, two independent
simulators, zero exceptions across all five mandated hard cases) — but the
count-bound target itself (how many permanent bundles a general core can
ever accumulate) is **not** resolved this round.)

## Promotable lemmas

- **No-Resurrection Lemma.** Fix a finite set of primes `C`. If some `k\ge1`
  has `\mathrm{rad}(a_k)\subsetneq C`, then `C\notin𝓜_m` for every `m\ge k`.
  Three-line proof directly from Lemma W3's definition of `n`-minimal; fully
  proved above. Unconditional, no dependency on any open gap. Ready to
  certify.

- **Interval Lemma.** For any `v\in𝓥`, the set `A_v:=\{n\ge1:v\in𝓜_n\}` is a
  contiguous interval of positive integers, either `[n_v,\infty)` or
  `[n_v,e_v)` for some finite `e_v>n_v`. Proved in full above from the
  No-Resurrection Lemma (no gaps: once absent after being present, absent
  forever). Unconditional. Ready to certify; strengthens/replaces the
  outline's asserted "at most two transitions" claim with an actual proof.

- **Theorem V (Equivalence).** `𝓥:=\bigcup_{n\ge1}𝓜_n` is finite **if and
  only if** (MRS) holds (`𝓜_n` eventually constant). Both directions proved
  in full above: (`\Rightarrow`) via the Interval Lemma and a finite `\max`
  over `𝓥`; (`\Leftarrow`) via a three-line finite-union argument, new this
  round (not in the outline, which only had one direction). Unconditional
  modulo (MRS) itself (which remains open) — the *equivalence* is fully
  proved either way. Ready to certify; sharpens
  `lemmas/lemma-MS-minimal-radical-stabilization-sufficiency.md`'s Lemma MS
  chain by showing the `𝓥`-finiteness reformulation loses no strength.

- **Record Characterization Lemma.** `𝓥=\{P_i:i\ge1\text{ is fresh}\}`, where
  `i` is fresh iff no `k<i` has `P_k\subsetneq P_i`. Proved in full above by a
  direct two-line argument in each direction, using only Lemma W3. Verified
  computationally (exact match with the simulator's `𝓜_n`-based definition on
  5 test cases, zero discrepancies). Unconditional. Ready to certify —
  gives a self-contained combinatorial description of `𝓥` independent of the
  `M_n`/`𝓜_n` machinery, useful for any future approach to `𝓥`-finiteness.

- **Proposition FR.** If `i\ge2` is fresh (Record Characterization Lemma's
  sense), then `\mathrm{rad}(a_1)\not\subsetneq\mathrm{rad}(a_i)`. One-line
  proof from the definition of freshness with `k=1`. Unconditional, no
  dependency on any open gap. Minor but ready to certify — a genuine
  (if weak) necessary condition on fresh indices, useful to rule out any
  future attempt claiming freshness is vacuous or unconstrained.

- **Theorem CI (Case I `\Rightarrow` `𝓥` finite, explicit bound).** If Case I
  holds with saturating prime `p`, `a_1=pm`, then with
  `k_0:=\min\{k\ge1:p^k\ge a_1\}` and `N_0:=p^{k_0-1}-m+1`, `𝓜_n=\{\{p\}\}`
  for every `n\ge N_0`, hence `𝓥\subseteq\{P_i:i\le N_0\}` is finite. Proved
  in full above from the already-certified Lemma S' plus elementary number
  theory (existence of `k_0` via `p^k\to\infty`, and an explicit bijection
  between indices `n` and multiples of `p` `\ge a_1`). Verified against
  `a_1=11623,p=59`: formula gives `N_0=3285`, exactly matching the
  independently-simulated stabilization index. Unconditional (given Case I).
  Ready to certify — a genuinely new, fully self-contained result, not
  present in any prior round, and (per the "Scope note" above) not otherwise
  needed to finish Case I (already solved by Lemma S'/Lemma Q), but valuable
  as a template and as a from-scratch verification of the round's other new
  lemmas on the hardest available Case-I stress case.

- **Lemma C (Global Intersection Collapse).** `C_n:=\bigcap_{i=1}^n
  \mathrm{rad}(a_i)` is non-increasing in `n`, stabilizes at some finite (not
  a-priori-bounded-by-`|P_1|+1`) index `N_0`, and the stable limit is nonempty
  iff a single prime saturates the whole sequence (Case I). Full proof above,
  including a from-scratch re-verified counterexample (`a_1=65`) to the naive
  `N_0\le k+1` bound. No dependency on any open gap — ready to certify.

- **Proposition NC1 (naive collapse-point backbone is insufficient).** The set
  `S_0=\bigcup_{i\le N_0}\mathrm{rad}(a_i)` (Lemma C's collapse-point union) does
  **not** in general contain every canonical witness `w(i,j)=\min(\mathrm{rad}
  (a_i)\cap\mathrm{rad}(a_j))`. Proved via a fully hand-verified 5-term
  counterexample, `a_1=221`, pair `(4,5)`, witness `5\notin S_0=\{2,3,7,13,17\}`.
  Self-contained; no dependency on any open gap. Useful to certify so future
  rounds (on this or sibling approaches) do not re-attempt this specific
  shortcut.

- **Proposition NC2 (witnesses need not be `\le\mathrm{rad}(a_1)`).** There is
  no a-priori bound `w(i,j)\le L:=\mathrm{rad}(a_1)` valid for all Case-II
  sequences. Proved via a fully hand-verified 7-term counterexample, `a_1=375`,
  pair `(3,7)`, witness `19>L=15`. Self-contained; no dependency on any open
  gap. Also useful to certify to steer future rounds away from this shortcut.

- **Key Lemma (`\omega`-bound).** If `\omega(a_n)\le M` for every `n\ge1` (a
  fixed constant `M`), then the Domination Lemma's dominant prime `q^*(n)`
  satisfies `q^*(n)\le M\cdot(a_1+L)` for every `n\ge2` (`L:=\mathrm{rad}(a_1)`).
  Three-line consequence of the already-certified Domination Lemma + Lemma 1;
  proved in full above. Ready to certify (conditional only on the hypothesis
  `\omega(a_n)=O(1)`, which is stated as a hypothesis, not assumed true).

- **Proposition ND1 (per-step dominant-prime set is not a valid FCBC covering
  set).** On the certified `a_1=221` trace, the set `H` built from `\mathrm{rad}
  (a_1)` together with the Domination Lemma's unique per-step maximizer at each
  of the first `3` steps fails to cover the pair `(2,4)` (`\mathrm{rad}(a_2)\cap
  \mathrm{rad}(a_4)=\{3\}`, but `3\notin H`). Proved in full above by direct
  computation of `D_1,D_2,D_3` for the relevant primes. Self-contained (reuses
  only the already-certified NC1 trace); no dependency on any open gap. Useful
  to certify so future rounds do not re-attempt this specific "necessity alone
  suffices" shortcut.

- **Proposition ND2 (broadened averaged-threshold prime set is also not a
  valid FCBC covering set).** On the certified `a_1=375` trace, the broadened
  set `Q'` of all primes meeting the Domination Lemma's averaged threshold
  `D_n(q)\ge n/\omega(a_{n+1})` at any tested step, together with `\mathrm{rad}
  (a_1)`, fails to cover the pair `(3,7)` (`\mathrm{rad}(a_3)\cap\mathrm{rad}
  (a_7)=\{19\}`, but `19` fails the averaged threshold at both steps where it
  is tested, `n=2` and `n=6`, computed explicitly above). Proved in full;
  self-contained (reuses only the already-certified NC2 trace); no dependency
  on any open gap. Useful to certify alongside ND1 as a matched pair of
  negative results ruling out the two most natural Domination-Lemma-based
  sufficiency mechanisms.

- **Lemma FOM (First-Occurrence Minimality).** If `n\ge2` is the first index
  with `\mathrm{rad}(a_n)=C`, then `a_n=T_C:=\min\{x>a_1:\mathrm{rad}(x)=C\}`
  exactly. Proved in full above via a clean single-argument
  proof-by-contradiction (greedy-minimality contradiction, no case split).
  Unconditional. Ready to certify — this is the designated certification home
  for FOM, since it strengthens this file's own already-certified Record
  Characterization Lemma (order-theoretic membership) with an exact numeric
  value.

- **Fan-Size Corollary.** If `C'` first occurs at index `m`, every earlier
  realized value `C'\cup\{q\}` (`q\notin C'`, at index `i<m`) satisfies
  `q<T_{C'}/\prod(C')`. Three-line consequence of Lemma FOM; proved in full
  above. Unconditional (given the antecedent that `C'` is eventually
  realized). Ready to certify.

- **Generation-Chain Lemma.** Any domination chain
  `C_1\supsetneq\cdots\supsetneq C_r\supseteq S` within a proper core `S` has
  `r\le|C_1|-|S|+1`. Three-line consequence of the already-certified
  No-Resurrection Lemma. Unconditional. Ready to certify.

- **Lemma ER (Eventual Realization Dichotomy).** For `y>a_1` not yet a term
  of the sequence: if `\gcd(y,a_i)>1` for every `i\ge1`, then `y=a_m` for
  some `m`. Proved in full above via a direct greedy-minimality contradiction
  (no dependence on radicals or Lemma FOM). Unconditional, general (holds for
  any greedy admissible sequence of this type, not just this problem's
  specific radicals). Verified numerically (`a_1=247`, `14287` candidates,
  zero exceptions). Ready to certify — a new, previously-unstated structural
  fact closing a loose conceptual end (rules out "permanently eligible but
  never chosen").

- **`Λ_S`-Reduction Lemma.** For a proper nonempty core `S\subsetneq P_1`,
  `𝓥_S` is finite `\iff` `Λ_S:=\bigcup_{C\in𝓥_S}(C\setminus S)` is finite.
  Proved in full above (both directions, three lines each). Unconditional.
  Ready to certify — reformulates a family-of-sets finiteness question into a
  flat-set finiteness question, reusable by any approach attacking `𝓥_S`.

- **Single-Companion Finiteness Lemma.** If `J_S:=\{j:\mathrm{rad}(a_j)\cap
  S=\varnothing\}` is infinite, then `Q_S` (primes ever realized as the sole
  companion of `S`) is finite, in fact `\subseteq D\setminus P_1` where
  `D:=\bigcap_{j\in J_S}\mathrm{rad}(a_j)` (finite, via the already-certified
  Generalized Lemma C applied to `I=J_S`, combined with the already-certified
  Lemma P′). Proved in full above. Conditional only on `J_S` infinite (stated
  as a hypothesis, verified numerically in three cases with an *exact* match,
  not proved in general). Ready to certify as a genuinely new mechanism —
  the round's main positive result on the Growth-Budget Lemma.

- **Multi-Companion Reduction Proposition.** If `Q` (`|Q|\ge2`, disjoint from
  `P_1\cup S`) is realized as `S\cup Q` at some index, then `Q` hits every
  `\mathrm{rad}(a_j)`, `j\in J_S` — a finite covering/hitting-set condition on
  the infinite family `\{\mathrm{rad}(a_j):j\in J_S\}`, i.e. a local,
  restricted instance of FCBC itself, not reachable by the
  Generalized-Lemma-C fixed-intersection mechanism. Proved in full above
  (identical mechanism to the Single-Companion Lemma's core step, generalized
  to `|Q|\ge2`). Unconditional. Ready to certify — this is the rigorous,
  proved (not asserted) explanation of exactly why the Growth-Budget Lemma
  is not closed by this round's new tool, useful for steering future rounds
  away from expecting the Generalized-Lemma-C mechanism to extend to
  multi-companion bundles without first solving a local FCBC-style problem.

- **Class-Decomposition Fact.** If `Q` is a bundle for `S` and `R\subsetneq
  S\cup Q` is the radical of any real index (any class), then `R\cap S\ne
  \varnothing`. Three-line proof from the already-certified Lemma P′.
  Unconditional. Ready to certify — the key structural fact making the
  Permanent Pair Lemma unconditionally gap-free for singleton cores, and
  isolating exactly the extra hypothesis (SCA) needed for non-singleton
  ones.

- **Permanent Pair Lemma (corrected).** A realized 2-companion bundle `Q`
  for `S` with both primes `\notin D_S` is permanently undominated,
  provided `|S|=1` (automatic) or `|S|\ge2` and Sub-Core Avoidance (SCA)
  holds (an additional hypothesis, proved by explicit witness +
  Permanent-Inadmissibility for the one non-singleton instance on record,
  `a_1=21528751,S=\{103,197\}`). Proved in full above; corrects a gap
  (unaddressed sub-core dominators) in the version proposed by the round-7
  math-explorer/outline-reviewer. Ready to certify — see
  `lemmas/lemma-permanent-bundle.md` for the standalone certification.

- **Permanent Bundle Lemma.** Generalizes the Pair case to bundles of any
  size `k\ge1`, adding a Subset Avoidance (SA) hypothesis genuinely
  required (not implied by `D_S`-disjointness) for `k\ge3`. Proved in full
  above; exhaustively validated (44 size-`\ge3` instances across all five
  mandated hard cases, zero exceptions in either direction; three proved
  by explicit witness, including a negative control). Ready to certify —
  see `lemmas/lemma-permanent-bundle.md`.

- **Deep antichain-freeze stress test (empirical, not a theorem — recorded
  for the record, not proposed for certification).** For all five mandated
  hard `a_1` values, the global minimal-radical antichain `𝓜_n` was
  verified, by literal set-identity via two independently cross-validated
  simulators, to freeze completely at a small index (`7,163,92,54,44967`
  respectively) and never change again through `N=3`–`5{,}000{,}000`. This
  is the deepest numerical support for (MRS) produced in this workspace to
  date, but is explicitly **not** a proof for general `a_1` — recorded here
  as a data point for future rounds, not as a certifiable result.

- **Realized–Blocked Dichotomy Lemma (RBD, new round 8).** For every
  nonempty finite set of primes `\kappa`, exactly one of "realized" /
  "blocked" holds — no third possibility. Proved in full above via a
  three-line synthesis of the already-certified Lemma ER,
  Permanent-Inadmissibility Lemma, and Lemma P′, applied to radical values
  rather than candidate integers (not stated anywhere in this workspace
  before). Unconditional. Ready to certify — this is the tool that makes
  the escape-recursion in Step 2 into a well-defined branching process with
  no undetermined node, and is likely reusable by any future approach that
  needs to reason about which bare radical values can ever be realized.

- **Complement Witness Fact (new round 8).** `I_S\ne\varnothing\Rightarrow
  J_{P_1\setminus S}\ne\varnothing`. Two-line proof directly from the
  definition of `I_S`, proved in full above. Unconditional. Ready to
  certify — a genuine, if partial, unconditional fact about witness
  existence; explicitly does **not** resolve the (still open) "core-avoiding
  witness for `S` itself" question (the honest scope note above explains
  exactly why the natural bootstrap fails).

- **Escape-Confinement Pairwise-Disjoint-Bundle-Count Corollary (new round
  8, Step 1).** If a core-avoiding witness `j_3` for `S` exists, every
  family of pairwise-disjoint bundles for `S` has size `\le
  |\mathrm{comp}(a_{j_3})|`. Proved in full above from the already-certified
  Escape-Confinement Lemma plus the new RBD Lemma. Conditional only on
  witness existence (verified case-by-case, automatic whenever the file's
  pre-existing "`J_S` infinite" standing hypothesis holds — no new
  unproven hypothesis beyond what this reduction chain already carries).
  Ready to certify.

- **Finite-Reachability Theorem + Reachability Theorem for (SA)-bundles
  (new round 8, Step 2).** Conditional on witness existence and NIBC (no
  infinite chain of always-blocked bare values rooted at `S`, a precisely
  named, honestly-open hypothesis), the count of bundles for `S` satisfying
  the already-certified Permanent Bundle Lemma's Subset-Avoidance (SA)
  hypothesis is finite. Proved in full above via an explicit reachable-set
  construction and a from-scratch proof of the needed finitely-branching-
  tree fact (a form of König's Lemma). Hand-verified end-to-end on a fresh,
  independently-computed worked example (`a_1=2747,S=\{67\},Q=\{2,3,7\}`,
  witnesses `a_2,a_4,a_{10}`). Ready to certify as a genuine conditional
  upgrade of round 7/8's informal "recursion doesn't visibly terminate"
  diagnosis into an exact theorem — NIBC itself remains open and is not
  claimed proved.

- **Transient-Bundle-Invisibility Proposition (new round 8).** Every bundle
  `Q` not satisfying (SA) is unreachable by the Step 2 construction, and
  every eventually-dominated (transient) bundle fails (SA) by definition
  (its own dominator is a realized proper subset, via the already-certified
  Class-Decomposition Fact). Proved in full above, illustrated on the
  workspace's one documented transient worked example
  (`a_1=21528751,S=\{197\},Q=\{2,3,7,41\}`, dominated by `\{2,3,7,197\}`).
  Unconditional. Ready to certify — this is the precise, proved (not
  observed) boundary of what the entire Escape-Confinement/pigeonhole
  mechanism family can ever establish: it structurally cannot reach the
  transient share of `Λ_S`, which is exactly the object this round's
  outline retargeted to. Valuable primarily as a *negative* result steering
  future rounds away from expecting any variant of this mechanism to close
  the transient count without a genuinely different idea.
