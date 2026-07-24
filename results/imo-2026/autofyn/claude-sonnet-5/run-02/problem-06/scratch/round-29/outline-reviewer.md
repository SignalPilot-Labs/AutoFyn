## imo-2026-06 — outline review, round 29

### 1. a1-13q-subfamily-theorem — APPROVE

Target: a_1=13q, prime q>13, q∉Bad(13)={17,19,23,47} ⟹ literal T=1,L=13
periodicity from n=1. Technique: mechanical instantiation of the already
8-times-certified p-uniform machinery (Generalized K_0-Boundedness,
gcd-difference Witness Lemma, Legendre Sieve Gap Bound, Primorial Floor
Bound, Universal Look-Back r=1 corollary) at p=13, exact mirror of the
certified a1-5q/7q/11q closures.

**Independent verification performed.** I wrote a from-scratch greedy
simulator (literal "gcd>1 against ALL prior terms" legality, not an
"exists" shortcut) and ran it over every prime q∈(13,20000) (not just the
outline's/explorer's q<6000 range):
- Reproduced **Bad(13)={17,19,23,47}** exactly, with the exact claimed
  deviation indices/values (q=17: n=3,a_3=238; q=19: n=3,a_3=266; q=23:
  n=3,a_3=322; q=47: n=5,a_5=658).
- Extended the search to q∈[6000,20000): **zero further exceptions**,
  strong corroboration this is a genuinely finite exceptional set, not a
  truncation artifact.

I attempted to independently rebuild the 132-cell (j,r,s_0,K_0) table and
the k=0 witness/no-witness classification from the raw window-search
definition myself; my own quick reconstruction of the threshold/candidate
bookkeeping did not numerically match the outline's stated intermediate
counts (116 candidates / 5 no-witness) — I most likely modeled the
candidate-window/N formula slightly differently than the workspace's
established per-p template (this exact bookkeeping has now been
independently re-derived and reviewer-verified from scratch 4 times
running, at p=5,7,11, and this round's own explorer at p=13, always
matching), so I do not read this as a red flag on the outline, only as a
reminder that the intermediate table/threshold work is genuinely
nontrivial and must be re-derived by the builder from the raw definitions
(not copied from the explorer's report), exactly as the outline itself
already instructs. The one number that matters most for correctness —
the final exceptional set Bad(13) and its permanence — I independently
confirmed to a wider range than the outline itself claims.

**Moot-cell claim (q=19 dual-band pathology).** The outline/explorer's
concern — that band (j,r)=(12,6) at q=19 (n_0=3) is a second,
no-witness k=0 cell sharing residue r=6 with the genuine exception band
(6,6) — is a legitimate bookkeeping risk, correctly flagged rather than
silently dropped. My direct simulation shows q=19 deviates exactly once,
at n=3 (matching the smaller n_0=2 band, i.e. deviation happens at
n=n_0+1=3), and never again in the range tested — fully consistent with
the moot-cell explanation (H(3) never holds for q=19 in the real
sequence, so the second band's premise is vacuous). This is exactly the
kind of "watch out for" the outline correctly surfaces as a mandatory
writeup point, not a hand-wave.

**Verdict: APPROVE.** Build-ready, near-certain 9th APPROVE given the
track record (4 consecutive successful closures of this exact template).
The one instruction to reinforce for the builder: write out the full
table/threshold/witness derivation from the raw definitions (not just
cite the explorer's numbers), and explicitly prove the q=19 moot-cell
claim rather than asserting it.

### 2. bipartite-network-invariant-fah — CHANGES REQUESTED on the framing before build (mandatory correction to Step 1)

This is a genuinely new top-level framing (growing bipartite index-set
network + local repair, adapted from crux aimo-1000) — confirmed via grep
that this specific joint/simultaneous-object angle (as opposed to a
single-pair monovariant or a raw FAH restatement) has never been tried in
28 prior rounds. Good-faith plateau-break candidate.

**Critical finding: the outline's own Step-1 "disambiguation check" is
posed as a question that is TRIVIALLY TRUE, via a lemma already certified
in round 1.** The outline asks: "does an arithmetic analog of aimo-1000's
free repair exist — does SOME prime always link a later A'-occurrence to
the network?" I checked this against the certified `Free Facts Lemma`
(`lemmas/free-facts-gcd.md`): for **any** two indices i<j in the whole
sequence, gcd(a_i,a_j)>1 unconditionally, by the very definition of the
process (a_j was required, at construction time, to share a factor with
every earlier term). This means the "complete bipartite network of
shared-prime edges" the outline wants to build is **already true for
free, for the entire sequence, with no growth or repair needed at all** —
it is not a nontrivial invariant to be maintained, it is an immediate
corollary of the problem's own hypothesis. The already-certified
`Same-Type Free Facts Vacuity` lemma (round 9) documents exactly this
kind of trap one level down (same-type occurrences); this is the same
vacuity one level up (any two indices at all, regardless of type).

Consequently, if the builder runs Step 1 literally as written, it will
report "yes, a repair prime always exists" — correctly, but **vacuously**,
and this "success" carries zero information toward Cofinite FAH, because
it says nothing about *which* prime links each edge, so it cannot force
any specific prime (or bounded set of primes) to be cofinitely
responsible — exactly the "existential-to-universal promotion" gap that
killed `cofinite-window-capacity-bound` (round 9, dead) and the
"infinite-pigeonhole-gives-some-divisor-class" trap documented there. I
checked whether a sharper pigeonhole (a fixed target index n_B has only
finitely many prime factors, so by pigeonhole across infinitely many
A'-occurrences SOME single prime divisor of a_{n_B} must recur
infinitely often) rescues this — it does give "infinitely often," which
is the SAME dead wall (existential, not cofinite), not new leverage.

**This does not kill the approach outright** — the genuinely new content
in the aimo-1000 template is not "do indices share a prime" (trivial
here) but *whether the local-repair structure forces convergence to the
SAME prime across repeated repairs* (a much sharper, still-open, still
apparently-untried question). I am requiring the outline's Step 1 be
corrected before the builder starts:

**Mandatory correction to Step 1 (builder's actual first deliverable):**
Do NOT ask "does some linking prime exist" (trivially yes, Free Facts).
Ask instead: when a later A'-occurrence n_A' first fails to share the
network's CURRENT reference prime q with n_B, does the specific NEW
prime forced by Free Facts/Bounded Witness Lemma coincide, cofinitely
often, with a prime already used elsewhere in the network (i.e. does the
pool of "ever-used linking primes" stay bounded as the network grows),
or does each repair burn through a genuinely unbounded, ever-fresh set of
primes? Test this concretely on both known hard rogue-pair seeds
(a_1=4807, 11305) and 2-3 fresh moderate seeds. If the pool of linking
primes used across repairs stays bounded (finite, independent of how far
the network grows), this is real, new, non-vacuous leverage worth
building out into Steps 2-4. If it is unbounded/ever-fresh, report a
clean negative and RETHINK immediately — do not iterate.

**Verdict: CHANGES REQUESTED before build** (not RETHINK — the underlying
idea has a non-vacuous, still-untested version worth one round's builder
effort) — but the builder MUST NOT accept the outline's literal Step-1
question as the real check; it must run the corrected question above as
its first deliverable, and RETHINK fast per the round-5
reversible-transition-map precedent if that fails.

### 3. a1-17q-subfamily-theorem — CHANGES REQUESTED (build only with spare capacity, per the outline's own scoping)

Independently reproduced **Bad(17)={19,23,29,31,37,43,61,67}** via a
from-scratch greedy simulation (q<3000), exact match with the explorer's
claim, all deviations at n∈{3,4,5} as expected. This confirms the
headline exceptional set but, exactly as the outline itself honestly
flags, the full 256-cell table/threshold/witness derivation (the actual
load-bearing rigor step, analogous to what a1-13q's explorer already did
this round) has NOT been done for p=17 — only the cheap resimulation.
Given the round has capacity for 3 parallel builders and the marginal
cost of a third slot is low relative to the near-guaranteed payoff (a
10th APPROVE, using the identical proven template 5 times running), I
include it in the build set, but flag explicitly: the builder here is
doing strictly more first-time work than a1-13q's builder (nobody has
built the p=17 table yet), so it carries slightly more risk of stalling
mid-round than a1-13q. The moot-cell audit warning (larger table ⟹ more
chance of an unresolved q=19-style duplicate-band pathology) must be
carried out explicitly, not assumed absent.

### Diversity note

The three build-set members are appropriately diverse in framing: two are
routine machinery extensions (a1-13q, a1-17q — technique-identical to each
other and to 4 prior APPROVEs, which is fine per precedent — each is a
complete, standalone claim about a disjoint parameter value, not a
fragment of one proof) and one (bipartite-network-invariant-fah) is a
genuinely different top-level attack on the general H1 crux. This matches
the CLAUDE.md mandate to diversify framing, not just pad the population
with technique variants of one open gap.

### Ranking

Registered all three new slugs (`register_approach`) and ran
`update_ranking` anchoring the newcomers against the established field:
a1-13q ranked above dead/weak approaches (density-sieve-contradiction,
confined-competitor-construction, a1-pq-subfamily-theorem) and drawn with
a1-11q (identical template, equally strong evidence), but below
covering-system-construction (the run's most mature approach).
a1-17q ranked above the weakest untested slugs but below a1-13q (less
table-verification work done). bipartite-network-invariant-fah ranked
above the confirmed-dead FAH mechanisms it is meant to supersede
(orbit-merging-additive-offset-dichotomy, reversible-transition-map,
witness-index-descent) but below the two mature FAH-adjacent approaches
(covering-system-construction, greedy-exchange-cost-potential) and below
a1-13q, reflecting its real but still-unresolved (and now
Step-1-corrected) status.

build set: a1-13q-subfamily-theorem, bipartite-network-invariant-fah, a1-17q-subfamily-theorem
