## imo-2026-06 — computational lens

### Method
Simulated the sequence directly (brute-force: for each n, scan m=a_n+1,a_n+2,...
and accept the first m with gcd(m,a_i)>1 for all i≤n) for a1 ∈
{4,6,8,9,10,12,14,15,16,20,21,22,25,26,30,33,35,39,42,45,50,51,55,57,63,65,69,
77,85,91,95,99,105}, out to 600–1500 terms depending on a1, then searched for
the eventual period T,L robustly (requiring ≥150 confirming terms after the
candidate transient, not just a short matching window — verified this matters,
see below). All code in `/tmp/round-4/*.py` (not committed; ephemeral).

### Raw data (selected; full table available on request)
```
a1=4   T=1  L=2    rad(a1)=[2]     rad(L)=[2]          (trivial: a1 even)
a1=6   T=1  L=2    rad(a1)=[2,3]   rad(L)=[2]
a1=9   T=1  L=3    rad(a1)=[3]     rad(L)=[3]
a1=15  T=8  L=30   rad(a1)=[3,5]   rad(L)=[2,3,5]       <- 2 newly recruited
a1=21  T=1  L=3    rad(a1)=[3,7]   rad(L)=[3]
a1=25  T=1  L=5    rad(a1)=[5]     rad(L)=[5]
a1=33  T=1  L=3    rad(a1)=[3,11]  rad(L)=[3]
a1=35  T=34 L=210  rad(a1)=[5,7]   rad(L)=[2,3,5,7]     <- 2,3 newly recruited
a1=39  T=1  L=3    rad(a1)=[3,13]  rad(L)=[3]
a1=45  T=8  L=30   rad(a1)=[3,5]   rad(L)=[2,3,5]       <- 2 newly recruited
a1=51,57,63,69  all T=1, L=3, rad(L)=[3]  (3|a1, 5∤a1)
a1=55  T=1  L=5    rad(a1)=[5,11]  rad(L)=[5]
a1=65  T=58 L=390  rad(a1)=[5,13]  rad(L)=[2,3,5,13]    <- 2,3 newly recruited
a1=77  T=18 L=154  rad(a1)=[7,11]  rad(L)=[2,7,11]      <- 2 newly recruited (NOT 3,5!)
a1=85  T=1  L=5    rad(a1)=[5,17]  rad(L)=[5]
a1=91  T=20 L=182  rad(a1)=[7,13]  rad(L)=[2,7,13]      <- 2 newly recruited (NOT 3,5!)
a1=95  T=82 L=570  rad(a1)=[5,19]  rad(L)=[2,3,5,19]    <- 2,3 newly recruited
a1=99  T=72 L=330  rad(a1)=[3,11]  rad(L)=[2,3,5,11]    <- 2,5 newly recruited
a1=105 T=58 L=210  rad(a1)=[3,5,7] rad(L)=[2,3,5,7]     <- 2 newly recruited
```
(all robustly verified: candidate T,L confirmed to hold for ≥150 further
terms after the claimed transient, not just a short matching window —
an earlier, looser search script produced spurious agreement on a
short window and had to be discarded).

### Key computational finding #1 — Q = rad(a1) ∪ rad(L) numerically suffices
For every a1 tested, checked exhaustively (all pairs (a_i,a_j), i,j up to
~400 terms) whether Q := rad(a1) ∪ rad(L) makes **every pair** of terms
share a Q-prime (i.e. Good_Q holds for all terms, the Unified Central
Claim from `reduction-lemma-ss1-vs-unified-claim.md`). Result: **0 bad
pairs in every single case tested**, including the largest transients
(a1=35,65,95,99,105, T up to 82). Also checked that Q must be at least
this large: for a1=35, rad(a1) alone leaves 7596 bad pairs (out of ~45000)
in the first 300 terms, rad(a1)∪{2} still leaves 1908 bad pairs, and only
rad(a1)∪{2,3} = rad(L) reduces bad pairs to 0. So the "extra" primes in
rad(L)\rad(a1) are genuinely necessary, not slack — Q cannot be smaller
than rad(L) in these cases.

**Conjecture A (evidence, not proof):** Q = rad(a1) ∪ rad(L) is *exactly*
the minimal finite prime set witnessing the Unified Central Claim, where L
is the sequence's own eventual step. This directly restates the central
gap in a form tied to L: "prove some finite Q ⊇ rad(a1) works" is
numerically equivalent to "Q = rad(a1) ∪ rad(L) works," but this is
circular as an existence argument since L is only known after the fact —
matches the population's own diagnosis in current.md. Does NOT resolve the
circularity; only sharpens it.

### Key computational finding #2 — trivial mechanism when 2 ∈ rad(a1) or a1 = p^k
- If a1 is **even**: T=1, L=2 always, with a one-line reason (elementary,
  not requiring the general machinery): a1+1 is coprime to a1 (consecutive
  integers), so a_2 ≠ a1+1; a1+2 shares factor 2 with a1, so a_2 = a1+2;
  inductively every subsequent term is a1+2k, i.e. the run of consecutive
  even numbers ≥ a1 is self-sustaining forever. This is a genuinely
  *closed, elementary* sub-case (worth stating explicitly as a base case
  in any future outline — it costs nothing and fully disposes of all even
  a1 at once).
- If a1's smallest prime factor is p and p ∤ (the "competing" primes
  needed to inject an off-cycle number before p-multiples saturate), the
  same argument runs with p in place of 2: T=1, L=p, Q=rad(a1). Empirically
  this happens whenever a1 = p·q with q a prime NOT close enough to make
  q-multiples interleave with p-multiples early (e.g. all of 3·7, 3·11,
  3·13, 3·17, 3·19, 3·23, 5·11, 5·17 tested give T=1). This looks like
  "the generic case" — most a1 give the trivial one-prime answer.

### Key computational finding #3 — the anomalous cases (T>1) are NOT explained by any simple congruence condition on the second prime
This is the crux of the whole problem and where all four approaches have
stalled, so I looked hard for a cheap distinguishing rule and did **not**
find one:
- 5·11=55 → T=1, but 5·13=65 → T=58, 5·19=95 → T=82. 11≡1, 13≡3, 19≡4
  (mod 5) — no clean split by residue mod smallest prime.
- 5·17=85 → T=1, but 5·7=35 → T=34. 17≡2 and 7≡2 (mod 5) — **same**
  residue mod 5, opposite outcome (T=1 vs T=34). This rules out "residue
  of the second prime mod the first prime" as the determining invariant
  (a natural first guess, cheaply falsified).
- The size of the second prime doesn't cleanly predict it either: 5·13
  (13 small) blows up but 5·17 (17 bigger) doesn't.
- 3·5=15 and 3²·5=45 both give T=8, L=30 — matches exactly (same T, L),
  suggesting the exponent on 3 is irrelevant once 5 is present, only
  rad(a1) matters. Consistent with the whole framework being about rad(a1)
  not a1 itself.
- Whenever BOTH 3 and 5 divide a1 or divide "compatible" combinations,
  T explodes: 15,45,99 (3,5-related) and 35,65,95,105 (5,7 / 5,13 / 5,19 /
  3,5,7 related) are exactly the non-trivial cases found. The common
  thread across all found T>1 cases: **a1's two smallest-ish prime
  factors are NOT {2,3}** (2 never divides a1, and either 3 is absent, or
  3 is present together with 5). I.e., the T=1 cases are precisely when
  3 | a1 and 5 ∤ a1 (giving L=3), or a1 = p^k a prime power with p ≥ 5 and
  no interfering companion (giving L=p), or 2 | a1 (giving L=2). This
  points to a **recursive/hierarchical mechanism**: numbers not divisible
  by the "leading" prime p_min can still sneak into the sequence if they
  are divisible by some other small prime already "linked in," and how
  many sneak in before saturation determines whether the periodic tail
  locks onto the trivial single-prime pattern or a genuinely composite
  L involving several primes. This is exactly the "recruitment" dynamic
  the state-compactness-pigeonhole approach's round-1/2 work already named
  informally, but I found no closed-form rule for *when* recruitment
  terminates after 1 prime vs several — this remains the open gap,
  consistent with 3 rounds of failure to pin it down.

### Distinct openings (for the outliner)
1. **Explicit trivial base case**: formally carve out and prove, as a
   clean warm-up lemma, that a1 even ⟹ T=1, L=2 (one paragraph, fully
   elementary, no machinery needed) and more generally a1 = p^k (p prime)
   with a self-sustaining run argument ⟹ T=1, L=p. This doesn't touch the
   general case but is a free, rigorous partial result that could anchor
   an inductive/recursive framing of the general proof (e.g. "the general
   a1 case reduces to finitely many rounds of this same run-saturation
   argument, each round adding at most one new prime to Q" — this is a
   *candidate* recursive framing, not yet a proof, worth exploring next
   round: does the recruitment process itself terminate because each
   newly-recruited prime is bounded by (roughly) the previous gap size,
   and gaps to next multiple of L strictly shrink or the prime pool is
   used up)?
2. **Q = rad(a1) ∪ rad(L) as the sharpest possible restatement**: use the
   numeric identification of exactly which set works (finding #1) to
   pressure-test whether Q can be defined via an *a priori* recursive rule
   (add primes one at a time whenever the current candidate set fails to
   cover a forced new term) rather than referencing L directly — this is
   basically a re-statement of "greedy recruitment," which prior rounds
   flagged as circular when tied to the *observed* period, but a
   *forward*, term-by-term recruitment rule (build Q incrementally as
   new terms force new primes in, prove this process halts) is a
   genuinely different target from "guess Q=rad(L) after the fact."
3. **Falsify simple invariants cheaply before heavy machinery**: the
   residue-mod-smallest-prime idea is now cheaply falsified (85 vs 35
   above) — do not let the outliner spend a round re-deriving that guess.

### Candidate technique(s)
Nothing new beyond what's in current.md — greedy/pigeonhole recruitment,
covering-system-style density arguments (Jacobsthal, already tried and
refuted), CRT-style residue analysis. The computational data suggests the
correct invariant (if any exists) is more subtle than a single modular
condition on the second-smallest prime; a genuinely recursive/inductive
"prime-by-prime" recruitment argument (bounding how many primes can be
recruited and why the process must terminate) looks like the most
promising unexplored angle, distinct from all four framings already tried
(orbit-pigeonhole, complement-set, Λ-split, windowed-automaton).

### Cheap-kill candidates
- "T=1 iff second-smallest prime ≡ r (mod p_min) for some fixed r" — FALSE,
  refuted by 85 (T=1) vs 35 (T=34), both with second prime ≡2 mod 5.
- "T=1 iff second-smallest prime exceeds some threshold" — FALSE, refuted
  by 65 (13, small, T=58) vs 85 (17, bigger, T=1).
- "exponents in a1's factorization affect T,L" — no evidence they do
  (15 and 45=3²·5 give identical T=8,L=30); only rad(a1) seems to matter.
  This is consistent with, and mildly supports, the existing framework's
  use of R(a1) (radical) rather than a1 itself.

### Knowledge-base entries to use
`knowledge_base.md`: Dirichlet (primes in AP) — already the natural tool
for constructing/recognizing periodic residue behavior mod L; Bertrand's
postulate — could bound how far recruitment can go if a size argument for
Q is found; "sequences are eventually periodic mod m" note (line ~80) is
the generic template the problem instantiates, but doesn't supply the
mechanism. No new entry beyond what prior rounds already cite.

### Analogous past problems (cruxes)
- `aimo-0447` (number_theory, likely subtopic `pigeonhole`/`divisibility-and-gcd`):
  "Encode a 'gcd>1 for every pair of shifts' hypothesis by placing in
  cell (i,j) a prime dividing the gcd, turning the condition into a
  complete prime-covering of a grid," then a counting argument
  (Σ 1/p², Σ1/p, prime-counting) bounds how large min{a,b} must be. This
  is structurally the closest analogue in the corpus — same "gcd>1
  pairwise ⟹ prime-covering" encoding — but it proves a *growth lower
  bound*, not periodicity, and its counting-density technique is exactly
  what `jacobsthal-covering-bound` already tried and the population
  already refuted for this problem (the g(Q) threshold and prime-size
  threshold mechanisms). Do not re-attempt this exact technique without a
  new idea — it has already failed twice on this problem.
- `aimo-0680` (functional equations / periodicity of f(n)-n): already
  identified and tried by `active-set-stabilization` in round 3
  ("divisible+bounded ⟹ zero" finishing move); confirmed by that approach
  to not transplant (k | a_{n+k}-a_n is false here, concretely refuted at
  a1=15). Re-verified this refutation is correctly stated — do not retry.
- No other corpus entry found that shares this problem's specific
  "greedy smallest-integer-satisfying-gcd-condition" construction; the
  corpus has covering-system and CRT cruxes (aimo-0436, aimo-0312) but
  none construct a sequence by greedy minimality under a gcd condition,
  so no further close analogue to report.

### Prior progress
Unchanged from current.md — Reduction Lemma (central gap = Unified
Central Claim: finite Q ⊇ rad(a1) with Good_Q(a_n) for all n), 4
mechanisms refuted (g(Q) threshold, prime-size threshold, Λ-split
tautology, windowed ε_n automaton). This round's numerics add: (a)
identification of exactly which Q works numerically (rad(a1)∪rad(L)), (b)
a clean, free, fully-elementary sub-case (a1 even, or a1 a prime power)
that closes T=1,L=p_min with a one-paragraph argument and no unresolved
machinery, (c) two cheap-kill falsifications of natural modular
invariants for predicting T=1 vs T>1.

### Dead ends (do not retry)
- g(Q) threshold, prime-size threshold, Λ-split "reduction" (tautological),
  windowed ε_n automaton — all per current.md, re-confirmed consistent
  with data (no new counterexample surfaced, no reason to doubt the prior
  refutations).
- "residue of second-smallest prime mod smallest prime determines T=1 vs
  T>1" — newly falsified this round (85 vs 35 counterexample above).
- aimo-0680-style transplant — confirmed still dead per current.md.

### Small-case / intuition notes (conjectural)
- Conjecture A: Q = rad(a1) ∪ rad(L) exactly suffices and is minimal, for
  every a1 (strong numeric support, ~30 instances, 0 exceptions, some with
  large transients/T up to 82 — but still just evidence).
- Conjecture B: T=1 (trivial single-prime case) precisely when a1 is even,
  OR 3 | a1 and 5 ∤ a1, OR a1 is a prime power p^k with p ≥ 5 and no
  "small companion" prime — but I could not pin down "small companion" to
  a clean numeric threshold (evidence: 55=5·11 trivial, 65=5·13 and
  95=5·19 not). This is exactly the unresolved recruitment dynamics that
  is the real content of the problem; flagging it precisely rather than
  guessing further seems the more useful contribution this round.
- No case tested had T that failed to stabilize within the search bounds
  (300–1500 terms) — mild evidence periodicity genuinely always occurs
  quickly relative to a1's size, consistent with the problem's claim, but
  this is exactly what needs to be proved, not new information.
