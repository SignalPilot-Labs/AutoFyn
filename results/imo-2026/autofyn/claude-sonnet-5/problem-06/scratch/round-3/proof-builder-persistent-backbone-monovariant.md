# proof-builder report — persistent-backbone-monovariant (round 3)

## Task
Build the round-3 revision of `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`,
addressing the outline-reviewer's CHANGES REQUESTED verdict: the ω(a_n)-boundedness
necessity algebra (dominant primes drawn from a bounded set) was verified sound, but
no mechanism was given for the necessity→sufficiency bridge — i.e. even a finite set of
"dominant" primes need not actually cover every pair i<j.

## What was done
1. Re-derived and confirmed the necessity-half algebra (Key Lemma ω-bound): if
   ω(a_n)≤M for all n, then the Domination Lemma's per-step dominant prime q*(n)
   satisfies q*(n)≤M·(a_1+L), giving a finite candidate set Q. Three-line, fully
   rigorous, depends only on the already-certified Domination Lemma + Lemma 1.
2. **Directly attacked the sufficiency bridge as requested**, testing two concrete
   candidate covering sets:
   - Q := literal per-step unique argmax primes (∪ rad(a_1)).
   - Q' := broadened set of every prime meeting the Domination Lemma's *averaged*
     threshold D_n(q)≥n/ω(a_{n+1}) at any tested step (∪ rad(a_1)).
   Both were tested computationally first (Python, exact integer factorization) to
   decide which was worth writing up, then **proved to fail by hand**, reusing the
   already-certified NC1 (a_1=221) and NC2 (a_1=375) counterexample traces so no new
   trace needed re-verification:
   - **Proposition ND1**: on the a_1=221 trace, the literal argmax set never
     recruits the prime 3, because at step n=3, D_3(17)=2 strictly beats D_3(3)=1;
     but rad(a_2)∩rad(a_4)={3} exactly, so the pair (2,4) is uncovered.
   - **Proposition ND2**: on the a_1=375 trace, the broadened averaged-threshold
     set never recruits 19, because at both steps where 19 is tested (n=2, n=6),
     D_n(19) falls short of the average threshold n/ω; but rad(a_3)∩rad(a_7)={19}
     exactly, so the pair (3,7) is uncovered.
   Both are fully hand-verified (all D_n(q) values computed explicitly from the
   certified factorizations), not merely numerically asserted.
3. Ran an exploratory (explicitly flagged as non-proof) density study: for a_1=247
   and a_1=375, prime-divisor densities D_n(p)/n split into a small set with stable
   positive density (matching known empirical covering sets) vs. all other primes
   with visibly decaying density. Recorded as a possible future direction, not a
   result — no proof that densities converge, and no argument from positive density
   to pairwise covering was found.
4. Updated the "What remains open" section to reflect that the gap is now better
   characterized: it is *not* that necessity was left unaddressed, but that the two
   most natural bridges from necessity to sufficiency are now proved false, and any
   future mechanism needs to be genuinely different (not a local/per-step
   Domination-Lemma argument).

## Outcome
Status remains `partial`. No claim of FCBC being solved or disproved. The round's
genuine contribution is: (a) the necessity algebra re-confirmed sound, (b) two new,
fully rigorous negative results (ND1, ND2) that close off the two most natural
"necessity implies sufficiency" shortcuts, matching CLAUDE.md's rule that finding and
proving a natural conjecture false is real progress. This is exactly the honest
answer the outline-reviewer asked for: a genuine bridge attempt was made and shown not
to work, rather than left as an unaddressed gap or silently declared solved.

## Promotable lemmas proposed for certification
- Key Lemma (ω-bound) — necessity half, ω(a_n)=O(1) ⟹ dominant primes drawn from
  a finite set.
- Proposition ND1 — literal per-step dominant-prime set is not a valid FCBC
  covering set (a_1=221 counterexample).
- Proposition ND2 — broadened averaged-threshold prime set is also not a valid
  FCBC covering set (a_1=375 counterexample).

File written: `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`
