## imo-2026-06 (lens: independent termination of the self-absorbing-core absorption chain)

### What N(S_k) precisely is
Fix a finite S ⊇ Q. `ρ_S(n) := P(a_n) ∩ S`. By the certified **Extended
Persistent-Type Pigeonhole** (`lemmas/extended-persistent-type-pigeonhole.md`,
generic in S), there is a finite nonempty set 𝒫'(S) of "S-extended-persistent"
types (each occurring at infinitely many indices) and a threshold N(S) — defined
as the LARGEST index n with ρ_S(n) ∉ 𝒫'(S) (0 if none) — beyond which every
ρ_S(n) lies in 𝒫'(S). N(S) exists by pigeonhole (finitely many types occur only
finitely often, sum of finite quantities is finite) but is only EXISTENTIALLY
finite: no certified tool computes it from a_1 (the workspace's own
Non-Constructivity observation, round 13, applies here verbatim — it was proved
for N₀/N₁/N₁'/N₂, and N(S) is the exact same shape of object).

The **absorption chain**: S_0 := S₀ (the unconditional Finite Core Theorem core),
S_{k+1} := S_k⁺ := S_k ∪ ⋃_{j=1}^{N(S_k)} P(a_j) — i.e. absorb the FULL
factorization (not just the S_k-restriction) of every one of the first N(S_k)
terms. S_k ⊆ S_{k+1} always (monotone chain of finite prime sets). "Terminates"
= reaches a fixed point (self-absorbing S* = S*⁺). Per the certified
**Termination Criterion Lemma**, this is exactly equivalent to (N(S_k))_k being
bounded.

### What a direct boundedness proof would need
1. **Some form of regularity of N as a function of the core S**, e.g.
   monotonicity (N(S) non-increasing, or eventually non-increasing, once S ⊇ S₀
   grows) or a bound N(S) ≤ f(|S|) for an explicit f. **No such fact is proved
   anywhere in the workspace.** `monotonicity-of-resolution.md` is a DIFFERENT
   statement (persistent-type-pair resolution, once achieved, is permanent under
   core enlargement) — it says nothing about how the *threshold index* N(S)
   itself behaves as S grows, and does not imply any monotonicity of N(S). This
   is the single most concrete missing structural fact — see "first concrete
   obstruction" below.
2. Given some such regularity, an inductive/pigeonhole argument bounding N(S_k)
   uniformly along the (a priori unboundedly growing) chain, OR an indirect
   argument (e.g. contradiction from S_k → an infinite set of primes, using the
   already-certified fact that a_n's own value only grows linearly in n so
   P(a_n) ⊆ primes ≤ n·a_1 — a magnitude constraint, not yet exploited here).

### Cheap-kill candidates tried / considered
- **"S_k eventually contains ALL primes ever appearing, so it stabilizes
  trivially"** — dead. The total prime-support set ⋃_{j≤n} P(a_j) is PROVEN
  unbounded (grows ~linearly in n, memory rule #6, independently reconfirmed by
  numerical trend below), so S_k can never legitimately "run out of new primes"
  this way; any boundedness proof must show S_k stops enlarging strictly
  BEFORE absorbing everything, not because there's nothing left to absorb.
- **Magnitude/size sandwich (a_n ≤ n·a_1, a_n ≥ a_1+(n-1))** — bounds the
  MAGNITUDE of terms absorbed at step k (primes ≤ N(S_k)·a_1) but says nothing
  about N(S_k) itself; this is exactly the class-blind-vs-class-sensitive gap
  (Sandwich Genericity Theorem / Escape-Cost Vacuity) already proven useless for
  the sibling FAH crux for structurally the same reason — a class-blind bound
  cannot discriminate "did stabilization already happen." Flagging this so a
  future round doesn't waste a build slot re-deriving the same vacuity in this
  new vocabulary.
- **Compactness/König/monovariant families** — round 15 already tried and killed
  these for FAH itself (memory rule #36); the same diagnosis applies here
  verbatim (no finite branching bound exists, since the "state space" 2^{|S_k|}
  is exactly the unbounded-in-principle object being questioned).

### Numerical probe (own simulation, this round — proxy method, evidence not proof)
Simulated the real greedy sequence (hand-rolled trial-division factorizer per
memory rule #32) for the two standard |F''|=2 rogue-pair seeds (4807, 11305) plus
two easy seeds (175, 35), and iterated a PROXY absorption chain: "persistent"
types approximated as those recurring ≥ min_count times in the tail
tail_frac-fraction of the sample; N(S) proxy = last sample index with a
non-recurring type.

Result: 175 and 35 (small-|Q| seeds where FAH already holds cleanly per the
standing test bed) show N(S_0) = 0 and the chain terminates in ONE round
trivially — consistent with round 15's positive computational picture. But on
the harder seeds:
```
a1=4807, 15000 terms: round0 |S|=3->N(S)proxy≈14875 (i.e. essentially the whole
  15000-term sample) -> absorbs 889 NEW primes in one round (|S| jumps 3->892)
  -> round1 N(S)proxy again pinned at the sample boundary (15000) -> |S| creeps
  to 902 -> loop terminated by my rounds budget, not by an observed fixed point.
a1=11305, 15000 terms: same shape, |S| jumps 4->1164->1170.
```
**Reading of this evidence (labeled conjecture/artifact, NOT a counterexample):**
the proxy's N(S)proxy value is pinned at the edge of whatever finite sample
window is used at every round tested — i.e. I could not observe genuine
stabilization of 𝒫'(S) within any computationally tractable window (up to
15,000 terms) for either standard rogue-pair test seed, even at the ORIGINAL
small core S₀ (|S₀| = 3 or 4). This is consistent with two very different
readings that this proxy CANNOT distinguish: (a) N(S₀) is genuinely enormous
(comparable to or exceeding 15,000) but still finite, matching the workspace's
own Non-Constructivity finding, or (b) an artifact of the tail-window proxy
undercounting persistence once the type-alphabet is large (2^|S| explodes, so a
15,000-term tail sample is too short to reliably witness "occurs infinitely
often" for finer types). Either reading is bad news for a *cheap* direct
boundedness proof: it rules out any hoped-for small explicit bound on N(S_k) for
exactly the seeds that matter (the |F'|,|F''|≥2 regime), and shows the
absorption chain's per-round growth is NOT small a priori — round 1 alone pulled
in ~890-1160 new primes on these two seeds, an order of magnitude beyond the
tiny 2-4-prime original cores. This is a genuinely new quantitative data point
not previously reported (prior rounds tested these seeds only at Q/S₀-level
FAH questions, not this absorption-chain object).

### First concrete obstruction (the actual missing lemma)
No certified or provable-on-sight fact establishes **any regularity of N(S) as a
function of S** — not monotonicity in either direction, not a bound in terms of
|S| or in terms of a_1. Without this, there is no scaffolding to run an
induction/pigeonhole over the chain (S_k)_k at all; one cannot even set up a
"suppose N(S_k) → ∞, derive a contradiction" argument, because nothing relates
N(S_{k+1}) back to N(S_k) or to |S_{k+1}|. Establishing such a monotonicity (or
at least a soft "N(S) does not increase once S ⊇ some threshold core" fact) is
the natural FIRST target for anyone attacking this sub-gap directly — and it
looks, from the numeric evidence above, to be at least as hard as bounding N(S₀)
itself on the hard seeds, i.e. no easier than the sibling recruitment-chain
question or FAH.

### Distinct openings (rival attack angles for the outliner)
1. **Attempt the missing monotonicity/regularity lemma for N(S) directly** —
   e.g. try to show N(S ∪ {p}) ≤ N(S) + (some explicit bound depending only on
   p, a_1) by a one-prime-at-a-time refinement induction (rather than jumping to
   the full S_k⁺ in one step). This is untried; it is a genuinely narrower,
   possibly more tractable target than boundedness of the whole chain at once.
2. **Give up on a general bound; restrict to a bespoke family** (matching the
   workspace's own round-14/15 escalation guidance) — e.g. try to prove
   termination specifically for the standard |F''|=2, multiplicity-1 test seeds
   (4807, 11305), where the Reduced-Alphabet Corollary already collapses the
   FAH question to one fixed divisor class; a parallel bespoke absorption-chain
   argument restricted to this family might be more tractable than the general
   claim.
3. **Look for an indirect (non-constructive) boundedness proof** that does NOT
   require computing/bounding N(S_k) itself — e.g. a compactness-style argument
   using that the chain of finite sets S_k, if unbounded, has a "limit"
   structure (union S_∞, an infinite set of primes each dividing some a_j) and
   try to derive a contradiction from properties of S_∞ directly (e.g. via
   density/growth-rate mismatch with the linear growth of a_n). Not attempted by
   anyone; likely runs into the same "class-blind vs class-sensitive" vacuity
   that killed the sibling sieve/density family for FAH (flag this risk to
   whoever tries it — check against `density-argument-vacuity-corollary.md`
   before investing effort).
4. **Reduce N(S)-boundedness to Confined-GCD-style single-fixed-witness
   information** (as several dead FAH mechanisms tried) — NOT recommended
   without a new ingredient; this shape (fixed witness / gcd against one term)
   is the most heavily mined and killed family (16 mechanisms) in the whole
   workspace, and nothing here suggests the absorption-chain object escapes the
   same class-blindness poison.

### Candidate technique(s)
No confident candidate found. The best lead is (1) above — a one-prime-at-a-time
refinement induction on N — genuinely untried, structurally distinct from the
(already-exhausted) gcd-pigeonhole family used against FAH itself, but the
numeric evidence above suggests even this narrower target may be hard on the
standard test seeds.

### Knowledge-base entries to use
- "Pigeonhole / extremal principle" (`knowledge_base.md`) — already the basis of
  every certified lemma in this chain; no further KB entry found relevant beyond
  what's already in use (checked KB for chain-condition/compactness/Noetherian-
  style entries — none exist beyond the generic pigeonhole/invariant bullets
  already exploited).
- No new KB entry surfaced specifically for bounding an iterated
  pigeonhole-threshold chain.

### Analogous past problems (cruxes)
None newly found this round beyond what's already on record (aimo-0514,
aimo-0016, aimo-0051, aimo-0134, aimo-0678, aimo-0030, aimo-0477 — all already
tried/exhausted per memory rules 3-4, 10, 13, 16-17, 20, 22, 25-28, 34). The
relevant crux subtopics for THIS specific sub-gap (`processes-and-algorithms`,
`invariants-and-monovariants`, `size-bounding-and-descent`,
`sequences-and-recurrences`) are the same ones already mined for the sibling
FAH/recruitment-chain crux; nothing in this dispatch's narrower focus (bounding
an iterated pigeonhole threshold specifically) turned up a new corpus match — the
closest shape (aimo-0514's "process as backward-deterministic map on finite
state space") requires an a priori finite/bounded state space, which is exactly
what's unknown here (the state space 2^{|S_k|} grows with the very chain we're
trying to bound), so it does not transplant.

### Prior progress
Termination Criterion Lemma (`lemmas/termination-criterion-lemma.md`, round 15,
certified) — the iff-reduction itself, not boundedness. Nothing further proved
toward N(S_k) boundedness anywhere in the workspace.

### Dead ends (do not retry)
- Any "S_k eventually absorbs everything" argument (contradicted by the proven
  unbounded total-prime-support fact).
- Any class-blind magnitude/sandwich argument for N(S_k) (same vacuity as
  `sandwich-genericity-theorem.md`/`escape-cost-vacuity.md`).
- Compactness/König/ergodic/additive-combinatorics framings (round 15, memory
  rule #36) — same "unbounded state space is exactly the open object" wall
  applies here too, re-confirmed by this round's reasoning, not re-simulated.

### Small-case / intuition notes (conjecture, not proof)
- On small-|Q| / already-FAH-clean seeds (175, 35), the absorption chain
  terminates trivially in one round (N(S₀)=0 in the proxy) — consistent with,
  but not new evidence beyond, round 15's positive n=1 computational picture.
- On the two standard hard test seeds (4807, 11305), the proxy could not detect
  stabilization of 𝒫'(S) within 15,000 sampled terms even at the tiny initial
  core S₀ (|S₀|=3 or 4), and one absorption round already pulls in ~900-1200 new
  primes. This is new, mildly discouraging evidence (labeled conjecture: not
  proof that N(S_k) is unbounded, since it may simply be a very large finite
  number beyond this sample's reach) that a *cheap* boundedness proof is
  unlikely to exist for exactly the seeds where FAH itself is hardest — suggests
  sub-gap (a), while logically distinct from FAH, may be comparably resistant to
  direct attack, not a soft target as one might have hoped from the "logically
  distinct" framing alone.
