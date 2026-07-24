## imo-2026-06

even-a1-full-periodicity-theorem: new
Target: the problem's actual claim — "there exist positive integers T, L such that
a_{n+T} = a_n + L for every positive integer n" — proved COMPLETELY and
UNCONDITIONALLY for the restricted subfamily of seeds with 2 | a_1. (This is
honestly scoped as a genuine but PARTIAL result: it settles the claim for an
infinite subfamily of a_1, not the general problem, which remains open for odd
a_1 pending FAH.)
Technique: direct elementary strong induction on n (no persistent-type/FAH
machinery at all — self-contained, uses only the problem's own minimality
definition and Free Facts-level gcd reasoning).
Skeleton:
  1. State the restricted claim: if 2 | a_1, then a_n = a_1 + 2(n-1) for every
     n ≥ 1, hence T=1, L=2 works literally from n=1 (not just eventually).
  2. Base case n=1: 2 | a_1 by hypothesis.
  3. Inductive step: assume 2 | a_i for every i ≤ n (i.e., a_i = a_1+2(i-1) for
     i≤n by the strong form). Consider the two smallest candidates for a_{n+1}:
     — by definition of the sequence, a_{n+1} is the smallest integer > a_n with
     gcd(a_{n+1}, a_i) > 1 for every i ≤ n.
  4. Candidate a_n+1 is ILLEGAL — gcd(a_n+1, a_n) = 1 always (consecutive
     integers are coprime), which alone violates the i=n constraint, for ANY
     seed (this fact needs no evenness at all).
  5. Candidate a_n+2 is LEGAL against every prior term simultaneously — since
     every a_i (i ≤ n) is even by the induction hypothesis, and a_n+2 is even,
     gcd(a_n+2, a_i) ≥ 2 > 1 for every i ≤ n.
  6. Since the smallest candidate is illegal and the second-smallest is legal
     against ALL constraints at once, minimality of a_{n+1} forces a_{n+1} =
     a_n+2 exactly, and it is even — closing the induction.
  7. Conclude: a_n = a_1+2(n-1) for all n ≥ 1 (closed form from steps 2-6), so
     a_{n+1} = a_n + 2 for every n ≥ 1 literally; T=1, L=2 verify the problem's
     claim exactly for this subfamily — state and verify explicitly (e.g.
     a_1=6: sequence 6,8,10,12,... — a_{n+1}-a_n=2 for all n, matches).
  8. Explicitly scope the result: this subfamily strictly contains and
     subsumes the existing certified "|Q|=1" special case (a_1 = 2^k) from
     `covering-system-construction`/`greedy-exchange-cost-potential` (item 10 in
     current.md's Current Best) — every a_1 = 2^k has 2 | a_1, but 2 | a_1 also
     covers a_1 = 6, 30, 210, 2·p for any odd prime p, etc. — so this is a
     genuine strict generalization, not a duplicate.
  9. Explicitly state what this does NOT do: it says nothing about odd a_1,
     where the general problem remains conditional on the still-open FAH crux
     (per `current.md`'s Current Best / the sole remaining gap (†)); this
     approach's own Status should read `partial` at the workspace level (it
     fully solves its own narrower target, but the workspace's overall claim is
     "for ALL a_1", still open for odd a_1).
Key lemmas (claim + mechanism):
  - Successor Determinism Lemma: when all of a_1,...,a_n are even, a_{n+1} =
    a_n + 2 exactly — because the two smallest candidates above (a_n+1, a_n+2)
    are respectively illegal/legal by bare consecutive-integer coprimality and
    common-factor-2 sharing, and minimality of the greedy definition admits no
    smaller legal choice than the smallest legal candidate found.
  - Uniform Evenness Lemma: 2 | a_1 propagates to 2 | a_n for all n — a direct
    corollary of the Successor Determinism Lemma by induction (step 6 above).
Open gaps: none for the stated restricted target — this is a complete, gap-free
proof of the 2|a_1 case. The open gap is external to this approach: the general
problem for odd a_1 (unaffected by this file).
Cases to cover: only one case (2 | a_1); the induction is uniform, no
sub-casework needed.
Watch out for: (i) do NOT overclaim this solves the general problem — the file's
own Status/Full-proof sections must scope the claim explicitly to "for all a_1
with 2 | a_1" and leave the workspace-level Status `partial`; (ii) verify the
closed form a_n = a_1+2(n-1) by an explicit small example in the write-up, not
just asserted; (iii) do not attempt to extend the mechanism to odd smallest
prime factors ≥ 3 — the round-16 explorer confirmed this is structurally
impossible (p-2 ≥ 1 intermediate candidates per step are not automatically
resolved by consecutive-integer coprimality alone), so the proof must state
this limitation rather than gesture at generalizing.

n1-periodicity-reconciliation: advance
Target: the problem's actual claim, in general — currently established
conditionally (dependency chain: FAH + existence/termination of a self-absorbing
core S* together imply literal n=1 periodicity, per the certified Self-Absorbing
Core Theorem + Literal n=1 Periodicity Theorem).
Technique: consolidation/write-up of the conditional theorem chain (per the
round-15 Rule's escalation option (a) — write up the current best result
rigorously and honestly with FAH as the sole open ingredient), NOT a new proof
attack this round; secondary, lower-priority stretch goal below.
Skeleton:
  1. Assemble, in one place inside this approach file, the FULL conditional
     theorem exactly as it currently stands, chaining together (with explicit
     citations to each certified lemma file): Free Facts → Persistent-Type
     Pigeonhole → Finite Core Theorem → Extended Persistent-Type Pigeonhole →
     [IF a self-absorbing core S* exists] Self-Absorbing Core Theorem → [IF
     FAH holds at S*] Universal Early Intersection Lemma → Literal n=1
     Periodicity Theorem. State the two, and only two, open hypotheses
     explicitly and precisely (their exact mathematical content, not just
     names): (H1) FAH at the eventual core: every two disjoint-base-type
     extended-persistent types intersect; (H2) the absorption chain S_0 ⊆ S_1
     ⊆ ... terminates (equivalently, per the certified Termination Criterion
     Lemma, the pigeonhole-threshold sequence N(S_k) is bounded).
  2. Cross-reference this round's new even-a1-full-periodicity-theorem result:
     note explicitly that for 2 | a_1 the general conditional chain is not
     needed at all (H1, H2 both vacuous/trivial — no disjoint persistent
     types exist since {2} is forced into every type), so the two results are
     complementary, not overlapping, contributions to the same workspace.
  3. (Stretch goal, only if time remains after step 1-2, do not force it) Check
     the one cheap, concrete idea flagged by this round's termination-lens
     explorer: for seeds where 2 ∈ Q (i.e. 2 | a_1 fails only conditionally on
     stronger seeds where 2 is already a "hub" prime shared by many types),
     does the absorption chain trivially terminate in 0 rounds because every
     type already shares 2? If yes on inspection this is a genuinely new,
     narrow, EASY corollary; if it requires new machinery, do not attempt it —
     just note it as a flagged idea for a future round, honestly undeveloped.
Key lemmas (claim + mechanism): none new required for step 1 (pure
consolidation of already-certified lemmas); if step 3 is attempted and
succeeds, its lemma would be: "if 2 ∈ Q, every persistent type contains 2 (by
Free Facts + Q ⊆ every base type), so no two persistent types are disjoint,
FAH is vacuously true and S* = S₀ trivially — because a shared prime 2 in every
type's support rules out disjointness by definition."
Open gaps: (H1) FAH itself — untouched this round, 17th+ mechanism NOT
attempted (per dispatch instruction not to re-attempt any of the 17+
confirmed-dead mechanisms and no new corridor was found this round); (H2)
core-chain termination — sharpened but not resolved (see
core-growth-monotonicity below for this round's dedicated attempt).
Cases to cover: none beyond the consolidation itself.
Watch out for: this round's task is explicitly NOT a new FAH mechanism attempt
— the builder must not silently smuggle in an 18th mechanism attempt under the
guise of "consolidation"; if the stretch goal (step 3) turns out to require new
unproved machinery, it must be reported honestly as open, not folded into the
write-up as if resolved.

core-growth-monotonicity: new
Target: the problem's actual claim, in general — via a dedicated, genuinely
untried attack on sub-gap (H2) (self-absorbing core existence/termination),
which is certified (Termination Criterion Lemma) to be logically distinct from
FAH — this does not re-attempt any of the 17+ dead FAH mechanisms.
Technique: one-prime-at-a-time refinement induction on the pigeonhole threshold
N(S), attempting a monotonicity/regularity bound N(S ∪ {p}) ≤ N(S) + f(p, a_1)
for an explicit f, per this round's termination-lens explorer's Opening 1
(explicitly flagged as untried and structurally distinct from the exhausted
gcd-pigeonhole family).
Skeleton:
  1. Fix finite S ⊇ Q and a single new prime p ∉ S. Consider S' := S ∪ {p}.
     By the certified Extended Persistent-Type Pigeonhole (generic in the
     core), 𝒫'(S') is finite and nonempty, with threshold N(S').
  2. Key structural claim: every S-extended-persistent type B ∈ 𝒫'(S) is
     refined, upon passing to S', into AT MOST TWO candidate sub-types: B
     (types where p never eventually divides) and B ∪ {p} (types where p
     eventually divides) — because ρ_{S'}(n) = ρ_S(n) ∪ (P(a_n) ∩ {p}), a
     binary refinement per index, so the alphabet 𝒫'(S') has size at most
     2·|𝒫'(S)|, a controlled, explicit blow-up.
  3. Attempt to bound N(S') in terms of N(S) and the (explicit, bounded) new
     alphabet size: try showing that, past index N(S), every index n has
     ρ_S(n) ∈ 𰭫'(S) already, so the ONLY remaining question for S'-persistence
     is whether p eventually settles into a fixed pattern within each existing
     S-persistent type — a strictly narrower pigeonhole (over an alphabet of
     size 2, not 2^{|S|+1}) applied AFTER index N(S). Attempt to give an
     explicit index bound for this narrower pigeonhole (standard finite-
     alphabet pigeonhole argument: with only 2 possible "does p divide"
     outcomes, some outcome recurs infinitely often within any single
     S-persistent type's infinite index set — this direction is free from the
     existing certified pigeonhole machinery; the OPEN part is whether the
     transition to "eventually only one outcome occurs" happens by an
     explicitly boundable index or only non-constructively).
  4. Honestly report the outcome: either (a) a genuine explicit or
     structurally-clean bound f(p, a_1) is found (real new progress on H2), or
     (b) the argument stalls exactly at the same non-constructive pigeonhole
     threshold as N(S) itself (i.e. this round's construction correctly
     narrows the alphabet but the INDEX bound remains existential-only,
     matching this round's own termination-lens explorer's numeric finding
     that N(S_0) is not observably small on the standard hard seeds
     4807/11305) — if so, this is a genuine, reportable negative result (an
     18th-family-adjacent but logically distinct dead end), not a failure to
     report.
  5. If (a) succeeds for single-prime steps, attempt (but do not force) the
     next layer: does iterating step 3 over the actual absorption chain S_0 ⊆
     S_1 ⊆ ... (which may add MANY primes per round, not one) give a bound on
     the TOTAL number of rounds via a sum/product of the per-prime bounds — if
     this reduces to assuming boundedness of the round count itself, flag it
     explicitly as circular and stop rather than force a claim.
Key lemmas (claim + mechanism):
  - Binary Refinement Lemma: passing from core S to S ∪ {p} refines each
    S-persistent type into at most 2 sub-types — because divisibility by the
    single new prime p is a binary (yes/no) fact appended to each index's
    existing S-restricted type, a direct consequence of the definition
    ρ_{S'}(n) = ρ_S(n) ∪ (P(a_n) ∩ {p}).
  - (Attempted, NOT assumed) Narrow Pigeonhole Threshold Bound: within any
    single fixed S-persistent type's infinite index set, the p-divides/
    p-doesn't-divide dichotomy stabilizes — standard pigeonhole guarantees
    SOME outcome recurs infinitely often, but an EXPLICIT index bound for when
    the OTHER outcome stops occurring is the genuinely open content; the
    builder must not conflate "recurs infinitely often" (free) with "settles
    permanently by an explicit index" (the actual open claim).
Open gaps: the entire explicit-bound question (step 3-4) is open going in;
this approach exists specifically to attempt it honestly and report the
result either way. Sub-gap H1 (FAH) is untouched by this approach by design.
Cases to cover: none beyond the single-prime-refinement analysis; if
attempted, the multi-prime chain extension (step 5) is explicitly a stretch,
not required for this round's deliverable.
Watch out for: the termination-lens explorer's numeric probe (this round)
found N(S_0) is not observably bounded within 15,000 sampled terms on the two
standard hard seeds (4807, 11305) — the builder should not be surprised or
treat it as a bug if step 3's construction also fails to produce a small
explicit bound on these seeds; a clean negative report (matching the
Termination Criterion Lemma's honest "iff N(S_k) bounded" framing, with no
false monotonicity claimed) is a valid, useful outcome. Do not let this
approach silently collapse into a disguised 18th FAH mechanism attempt — it
must stay strictly about the threshold-index N(S), never about which specific
prime resolves a specific rogue pair.

build set: even-a1-full-periodicity-theorem, n1-periodicity-reconciliation, core-growth-monotonicity
