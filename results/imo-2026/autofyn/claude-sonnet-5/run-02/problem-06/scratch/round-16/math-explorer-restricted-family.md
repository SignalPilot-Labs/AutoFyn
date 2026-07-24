## imo-2026-06

- **Headline finding (new, not previously documented anywhere in 15 rounds of
  current.md / approaches / lemmas — grepped and confirmed absent): the entire
  family `2 | a_1` is COMPLETELY, TRIVIALLY, UNCONDITIONALLY solved, with NO FAH,
  NO persistent-type machinery, NO recruitment process needed at all.**

  Claim: if `2 | a_1`, then `a_n` is even for every `n ≥ 1`, and in fact
  `a_{n+1} = a_n + 2` for every `n ≥ 1` (period `T=1`, gap `L=2`, holding
  *literally from n=1*, not just eventually — this also for free closes the
  secondary n=1-periodicity gap for this whole family).

  Proof sketch (2 lines, airtight, verify-by-hand): induct on n. Base case `2|a_1`
  given. Inductive step: assume `2 | a_i` for all `i ≤ n`. Candidate `a_n+1` is
  odd and `gcd(a_n+1, a_n) = 1` (consecutive integers are always coprime), so
  `a_n+1` is illegal (fails the `i=n` constraint) — this holds for ANY seed, not
  just even ones, it's just usually not decisive. Candidate `a_n+2` is even, and
  since every `a_i` (`i≤n`) is even by the induction hypothesis,
  `gcd(a_n+2, a_i) ≥ 2 > 1` for every `i ≤ n` — so `a_n+2` is legal against
  *every* prior term simultaneously, with zero extra work. Since `a_{n+1}` is by
  definition the smallest integer `> a_n` satisfying all constraints, and we've
  shown the two smallest candidates are (illegal, legal) in that order,
  `a_{n+1} = a_n+2` exactly, and it's even, closing the induction. ∎

  Verified numerically (python, exact greedy simulation, `math.gcd` + trial-division
  factorizer per round-14's tooling note) on `a_1 ∈ {6,10,14,22,26,34,38,46,58,62,
  74,12,20,24,40,18,300,210,2310,450,96,270,...}` spanning `ω(a_1)` from 1 to 5 and
  various prime combinations including `p=2` paired with large primes — in EVERY
  case, over 1500-3000 sampled terms, the gap sequence is the constant `{2}`, zero
  exceptions, matching the proof exactly (not just "cofinite" — literally constant
  from the first step). This is not merely a conjecture supported by data; the
  2-line induction above is a complete, rigorous, self-contained proof requiring
  only Free Facts-level reasoning (no persistent types, no Q-types, no core
  primes, no FAH). It reuses NONE of the certified machinery — it is a genuinely
  disjoint, self-sufficient argument.

  **Why this is the right target for this round's mandate.** It IS a restricted
  family, but the axis is "smallest prime factor of `a_1` equals 2" rather than
  `ω(a_1)`. It generalizes and subsumes half of the existing trivial `ω(a_1)=1`
  special case (item 10 in current.md's "Current best": that's the sub-case
  `a_1 = 2^k`) to ALL `ω(a_1) ≥ 1` as long as `2 | a_1` — i.e. it is strictly
  stronger and covers infinitely many seeds the existing trivial case does not
  (e.g. `a_1 = 6, 30, 210, 2·p` for any odd prime `p`, etc.), all with the SAME
  2-line proof.

  **Why the mechanism does NOT generalize to any other prime.** The proof's sole
  engine is that there is exactly ONE integer (`a_n+1`) strictly between `a_n`
  and the next even number `a_n+2`, and that one integer is automatically illegal
  by bare consecutive-integer coprimality against `a_n` itself — no
  factorization analysis needed. For any other prime `p ≥ 3` playing the role of
  "smallest prime factor," there are `p-1 ≥ 2` candidates between consecutive
  multiples of `p`, and only the FIRST of those (`a_n+1`) is automatically
  illegal by the same trivial coprimality argument; the remaining `p-2` candidates
  (`a_n+2, ..., a_n+(p-1)`) are neither automatically legal nor automatically
  illegal — legality depends on whether they happen to share some other prime
  factor with all `n` prior terms, which is exactly the FAH-flavored question
  the workspace has been stuck on for 10 rounds. Verified computationally: for
  odd-`a_1` seeds (`a_1=15,35,91,143,187,209,247,...`), gap sequences are NOT
  constant (multiple distinct gap values occur), consistent with this diagnosis.
  So `p=2` is uniquely special — this is not an oversight in scope but a genuine
  structural fact (`2` is the only prime with "gap 1" between multiples).

  **Consequence for framing the open problem.** The FAH crux (and the whole
  covering-system-construction / persistent-type apparatus) is now known to be
  needed ONLY when `a_1` is ODD (`2 ∤ a_1`). This is a clean, provable
  narrowing: half of the seed space (by the natural "is `a_1` even" split, not
  a density claim — a literal dichotomy) is fully disposed of by 2 lines of
  elementary reasoning. This does not touch or weaken the general odd-`a_1` FAH
  crux itself, but it is a genuine, certifiable, standalone theorem the outliner
  should turn into an approach this round (near-zero risk, trivially buildable,
  and a real Elo-worthy addition to the population — likely to be the strongest
  new content this round given FAH itself remains stuck).

- **A second, weaker, and NOT fully resolved observation (worth noting, lower
  priority):** among odd `a_1` with `ω(a_1)=2`, `Q=\{p,q\}` (`p<q` odd primes), a
  numerical sweep over 27 squarefree/prime-power seeds found a genuine dichotomy:
  many seeds (e.g. `a_1=55,21,33,39,51,85,115,119,133,161,185,205,215,235,253`)
  show the LARGER-prime-only type `\{q\}` occurring ZERO times in the sampled
  tail (persistent types are only `\{p\}` and `\{p,q\}`, which are NOT disjoint,
  so FAH is vacuous and the existing finish applies unconditionally for these
  specific seeds!) — while other seeds (`a_1=15,35,77,91,143,187,209,247,65,95,
  221,299`) show BOTH `\{p\}` and `\{q\}` persisting with substantial frequency
  (genuine disjoint-type pair, FAH-relevant). I could NOT find a clean closed-form
  criterion on `(p,q)` distinguishing the two regimes in the time available (it
  is not simply `q/p` ratio, nor `q mod p`, nor which is "close to a power of the
  other" — e.g. `a_1=65` (`p=5,q=13`, ratio 2.6) has `\{q\}` persistent while
  `a_1=55` (`p=5,q=11`, ratio 2.2) does not). This looks like a genuinely
  emergent dynamical property, not a simple arithmetic one, so I do NOT recommend
  building an approach around finding this criterion this round — flagging it
  only as a secondary, harder, and less obviously tractable restricted-family
  candidate for a future round if the `2|a_1` family gets fully closed out and
  more "cheap wins" are wanted.

- Distinct openings: (1) [PRIMARY, recommend build] `2 | a_1` full elementary
  closed-form theorem — self-contained, no FAH dependency, ready to write as a
  complete approach/lemma this round. (2) [secondary, not build-ready] an
  empirical vacuous-FAH dichotomy among odd `ω(a_1)=2` seeds (larger prime's
  solo type sometimes never persists) — real but lacks a provable criterion yet;
  would need real investigation before it's buildable, not just "run the numbers
  again."

- Candidate technique(s): pure elementary induction (no knowledge-base entry
  needed beyond the problem's own minimality definition) for the `2|a_1` family.

- Cheap-kill candidates: the "smallest prime = p ≥ 3" generalization is
  concretely ruled out (not just conjectured) by the same consecutive-integer-
  coprimality argument failing to cover the `p-2 ≥ 1` intermediate candidates —
  don't waste builder time trying to extend the 2-line proof past `p=2`.

- Knowledge-base entries to use: none needed for the `2|a_1` theorem itself (it's
  self-contained); if the outliner wants to connect it back to the existing
  population's vocabulary, it can be phrased as "Free Facts, Q={2,...}: the
  persistent type is forced to be a superset of {2} for literally every n, so no
  disjoint persistent-type pair can ever exist — FAH vacuous" using the existing
  Free Facts / persistent-type definitions (`lemmas/free-facts-gcd.md`,
  `lemmas/persistent-type-pigeonhole.md`), but the direct 2-line induction is
  simpler and doesn't need this framing at all.

- Analogous past problems (cruxes): none of the cruxes surfaced in 15 rounds of
  crux-mining are relevant here — this finding is elementary and doesn't need a
  crux transplant; it was found by direct simulation/induction, not corpus
  mining. (Did not re-run corpus queries this round since the finding is
  self-contained and doesn't need external technique import — spent the time
  budget on verifying the claim numerically across many seeds instead, per the
  dispatch's emphasis on "brute structural argument, not just numerical
  verification," which the 2-line proof above satisfies.)

- Prior progress: unchanged from round 15 — FAH/Symmetric FAH/Cofinite FAH/EEA
  remains the sole open crux for ODD `a_1`, 16 mechanisms killed, current best
  chain of certified lemmas intact (Finite Core Theorem, Confined-GCD Lemma,
  Singleton-Side FAH, Reduced-Alphabet Corollary, Self-Absorbing Core Theorem,
  Literal n=1 Periodicity Theorem, Termination Criterion Lemma, No-Restart Lemma,
  etc. — all as summarized in current.md/run_state.md). This round's finding is
  ADDITIVE (a new fully-solved family) and does not change the status of FAH
  itself.

- Dead ends (do not retry): the "smallest prime = p ≥ 3" generalization of the
  2-line even-seed argument (structurally impossible, see above — the
  consecutive-coprimality trick only kills ONE of the `p-1` intermediate
  candidates when `p ≥ 3`, leaving `p-2 ≥ 1` genuinely open candidates per step,
  which is exactly where FAH-level difficulty re-enters). Do not re-propose this
  without a fundamentally different mechanism for the intermediate candidates.

- Small-case / intuition notes: (1) PROVED, not conjectured: `2|a_1 ⟹ a_n=a_1+2(n-1)`
  for all `n≥1` (2-line induction above; numerically confirmed with zero
  exceptions on ~20 seeds up to 3000 terms each, `ω(a_1)` from 1 to 5). (2)
  CONJECTURE only (no proof found): among odd `ω(a_1)=2` seeds, whether the
  larger prime's solo type persists appears to depend on the full dynamical
  history, not a simple closed-form function of `(p,q)` — evidence is a 27-seed
  sweep, genuinely inconclusive on a criterion, flagged as lower priority.
