## imo-2026-06

- Distinct openings explored (restricted-family lens only — no attempt at the general FAH crux):
  1. **Does "min(Q) = p ≥ 3" (companion of the already-solved p=2 case) admit the same
     2-candidate-dichotomy induction?** Tested directly. Answer: NO, not cleanly — see
     numeric findings below. The mechanism used for `2|a_1` (an always-illegal `a_n+1`
     plus a provably-always-legal `a_n+2`) genuinely needs `p=2` for the *second* half;
     for `p≥3` there is no analogous "uniform residue-class" argument, because staying
     `≡0 mod p` does not make `a_n+2` divisible by `p` (only `a_n+1` would be, and that's
     already illegal for the trivial coprimality reason, giving zero new information).
  2. **Is there a clean sub-criterion on the companion prime(s) of a_1 (e.g. "smallest
     prime factor p, second-smallest prime factor q, and some congruence pq ≡ ... ")
     that predicts whether the pattern `a_n = a_1 + p(n-1)` holds forever?** Tested
     numerically across many `p·q` and `p·q·r` seeds (below). No clean criterion found;
     whether the pattern holds appears to depend on fine arithmetic coincidences of the
     actual seed, not a formula in `p, q` alone.
  3. **Is the already-solved `|Q|=1` (prime-power `a_1`) case the ONLY clean closed-form
     family, with `2|a_1` as the unique exception among `|Q|≥2` cases?** Numeric evidence
     strongly supports this: prime powers (any prime, any exponent) always give
     `a_n = a_1 + p(n-1)` forever (already certified round 3, "|Q|=1 special case"), and
     `2|a_1` (any `ω(a_1)`) always gives `a_n = a_1+2(n-1)` forever (round 16, certified).
     For every other tested `ω(a_1)=2,3` odd seed, the pattern EITHER holds (empirically,
     no proof) or breaks at a small index, and which one happens is seed-specific, not
     omega-specific or prime-specific.

- Candidate technique(s): none beyond what's already certified — this lens does NOT
  surface a new mechanism for the general FAH crux. The 2|a_1 proof's core idea
  (find an interval [a_n+1, a_n+d] where exactly one point is forced-legal by a uniform
  divisibility invariant and everything below is forced-illegal by bare coprimality)
  is structurally the *only* clean case because `d=2` leaves ONE candidate to check and
  bare coprimality with `a_n` alone already kills it. For `p≥3`, `d=p` leaves `p-1≥2`
  candidates between `a_n+1` (killed by coprimality with `a_n`) and the next multiple of
  `p`; deciding legality of those intermediate `p-2` candidates requires knowing whether
  they share a factor with *some* earlier term — exactly the same "does some earlier
  term already carry the right factor" question that FAH is about. So this restricted-
  family search independently re-confirms (not just repeats) memory rule 32's warning
  from a genuinely fresh numeric angle: the well is not just "hard to extend past p=2",
  it is *provably the same kind of question* as the general crux, with no shortcut.

- Cheap-kill candidates: **parity/residue observation confirmed as the sole clean
  invariant.** For `min(Q)=p`, the residue-class argument only closes cleanly when
  `p=2` because a length-2 window has a unique intermediate integer. For any `p≥3` a
  parity-style argument leaves `≥2` intermediate integers unaccounted for — this is a
  clean, provable NO-GO for the whole "generalize 2|a_1 verbatim" idea (not just
  empirically discouraging, but structurally forced by counting candidates in the
  window `(a_n, a_n+p]`).

- Knowledge-base entries to use: none new; this is a pure elementary-induction /
  small-case investigation, same toolkit as the already-certified Even-Seed Literal
  Periodicity Theorem. No FAH/persistent-type machinery needed or applicable here.

- Analogous past problems (cruxes): none searched this round (out of scope for this
  lens — pure numeric/structural probe of restricted a_1 families, not a technique
  transplant question). Round 12/14/15 already surveyed the corpus broadly for
  FAH-adjacent techniques; this lens is orthogonal (it's about scoping a sub-case, not
  about a proof technique).

- Prior progress: `lemmas/even-seed-literal-periodicity-theorem.md` (2|a_1, T=1 L=2,
  literal from n=1, certified APPROVE round 16) is the only genuinely clean restricted
  family found so far, plus the older `|Q|=1` (prime-power a_1) special case (round 3,
  gap = p forever, also literal and clean, reconfirmed numerically this round for
  primes 3,5,7,11 and their powers).

- Dead ends (do not retry):
  - **"3 | a_1 admits a clean induction like 2 | a_1"** — FALSE as a general claim.
    Numerically: `a_1 = 3p` gives constant gap 3 forever for `p = 7,11,13,17,19,23,
    29,31,37,41,43,47` but FAILS (gap deviates from 3 almost immediately) for `p=5`
    (`a_1=15`) — confirmed by direct simulation (gaps `[3,2,4,6,6,4,2,3,...]`, period-7
    pattern, matches the already-known `a_1=15` example used elsewhere in the
    workspace for the No-Restart Lemma). So "3 | a_1" alone is not a sufficient
    condition and there is no clean single extra hypothesis on the companion prime `p`
    found that fixes this (see next item).
  - **"companion prime just needs to avoid p=5" as a fix for the 3|a_1 family** — FALSE.
    `a_1 = 3·11·13 = 429` (no factor of 5 at all) STILL breaks the constant-gap-3
    pattern (gap sequence `[3,3,3,2,4,6,6,6,3,3,6,6,6,6,3,...]`), while `3·7·11=231` and
    `3·7·13=273` stay constant 3 forever. So it is not simply "5 is the bad prime";
    triples of primes can break the pattern even without 5 present. No simple
    replacement criterion (congruence condition on the companion primes mod small
    numbers) was found to separate the break/no-break cases in the limited search
    done this round.
  - **"5 | a_1 (as smallest prime factor) admits a clean induction"** — FALSE, same
    irregular pattern: `a_1=5p` gives constant gap 5 forever for `p=11,17,23,29,37,41,
    43,47,53,59` but breaks for `p=7,13,19` (`a_1=35,65,95`).
  - Do not propose "the pattern holds whenever ω(a_1)=2 and companion prime is large
    enough" — false as literally stated; largeness alone doesn't predict it (`p=37,41`
    with base 3 works but so does `p=7,11,13`; the *specific pair* `(11,13)` with base 3
    breaks it — magnitude of the companion primes is not the discriminant).

- Small-case / intuition notes (all labeled CONJECTURE / numeric observation only,
  not proofs):
  - Prime-power `a_1` (any single prime p, any exponent): conjectured (matches the
    already-certified round-3 |Q|=1 result) `a_n = a_1 + p(n-1)` for all n, literally,
    always. Reconfirmed numerically for p=3,5,7,11 up to 400 terms.
  - `2 | a_1` (any ω): certified, `a_n=a_1+2(n-1)` for all n (round 16).
  - For odd `min(Q)=p≥3` with `ω(a_1)≥2`: whether the analogous `a_n=a_1+p(n-1)`
    pattern holds forever is seed-dependent and NOT determined by `p` or `ω(a_1)` alone;
    roughly 60-80% of the small `p·q` seeds tested stayed constant, but the exceptions
    (15, 35, 65, 95, 105, 165, 429, ...) show no obvious common structural marker beyond
    "eventually some intermediate candidate in `(a_n, a_n+p)` finds an earlier term to
    share a factor with" — which is exactly a disguised instance of the general FAH-type
    question (does an early witness's factorization align with a later candidate's).
    This numerically reinforces (does not newly prove) the standing diagnosis that the
    `2|a_1` mechanism is a genuine one-off (unique because window size 2 leaves nothing
    to check), not the first member of an extendable family. No new mechanism or
    corridor for the general FAH crux surfaced from this lens.
