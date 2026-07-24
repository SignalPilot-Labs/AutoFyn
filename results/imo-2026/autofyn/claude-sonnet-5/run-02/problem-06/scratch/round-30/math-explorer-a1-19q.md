## imo-2026-06 (lens: a1=19q build-readiness, next small-prime subfamily)

- Distinct openings:
  1. **Direct instantiation of the certified p-uniform machinery at p=19** (the
     proven route, 10/10 success rate at p=3,5,7,11,13,17): reuse
     `a1-pq-subfamily-theorem`'s symbolic reduction verbatim, substitute p=19,
     build the (p-2)x(p-1)=17x18=306-cell `(j,r)` table via
     `s_0(j,r)=j*r^{-1} mod 19`, `K_0(j,r)=19+s_0(j,r)`, close `r=1`'s `k=0`
     layer for free via the certified Universal Look-Back Witness Identity's
     r=1 corollary, close the remaining cells via the sufficient-window
     criterion / Legendre-Sieve + Primorial-Floor toolkit, hand-verify the
     (here: 7) genuine diagonal exceptions. This is a pure scale-up, no new
     idea needed — build-ready today.
  2. **Elementary closed-form check of the diagonal exceptions** (new this
     round, not previously spelled out as cleanly): for the diagonal band
     `j=r`, `s_0=1`, `K_0=p+1=20`, `n_0=1+(q-r)/19`, so the Case-(b) window
     is the *consecutive-integer* interval `{q+1,...,q+n_0-1}` of length
     `(q-r)/19`. Since `q` is odd, `q+1` is always even, so `2 | gcd(q+1,20)`
     — meaning the length-1 window (`q=r+19`, i.e. the very first prime in
     residue class `r` above 19) is *automatically* a genuine exception with
     zero extra casework: a one-line, non-computational proof of the "first
     representative in each diagonal residue class is always bad" fact. For
     longer windows, the criterion "does every element of
     `{q+1,...,q+n_0-1}` share a factor with `20=2^2*5`" reduces to checking
     divisibility by 5 among the odd elements (`q+2,q+4,...`) — a fast,
     purely elementary sieve, avoiding any Legendre-sieve/Primorial-Floor
     machinery for the *small*-window diagonal cells specifically. This could
     shorten the proof's §6 (hand-verification of exceptions) into a clean
     2-3 line general argument instead of one paragraph per exception (as
     done in a1-11q/13q/17q).
  3. **Never mind the diagonal-only conjecture (Minimal-Window Necessity) —
     it's still open**; p=19 is another data point (0 non-diagonal exceptions
     found among 2254 primes tested to 20000) but this does NOT close the
     open conjecture from `a1-pq-subfamily-theorem`'s round-26 build. If the
     outliner wants to advance the *general* pq-family theorem (not just
     another single-p instance), this remains the sharpest lever: proving
     "if s_0(j,r)>=2, then for q above a small threshold a Case-(b) witness
     always exists at k=0" would collapse ALL future p-instantiations
     (19, 23, 29, ...) from O(p^2) cell-by-cell work to O(p) diagonal-only
     checks. Nobody has attempted this seriously since round 26; still open.

- Candidate technique(s): direct instantiation of the certified p-uniform
  machinery (Generalized K_0-Boundedness, Legendre Sieve Gap Bound, Primorial
  Floor Bound, Universal Look-Back Witness Identity r=1 corollary) at p=19,
  exactly the a1-11q/13q/17q template. Elementary parity/mod-5 divisibility
  argument (opening 2 above) as an optional simplification for the diagonal
  exception proofs.

- Cheap-kill candidates: the diagonal-band closed form
  `n_0(j,r)=1+(q-r)/19`, window `{q+1,...,q+n_0-1}`, `K_0=20=2^2*5` — checking
  parity + divisibility-by-5 of the window elements is a two-second check
  that immediately identifies/certifies genuine exceptions without any sieve
  machinery, for the diagonal cells specifically. (Does not help the 299
  non-diagonal cells, which still need the full sufficient-window/threshold
  toolkit as in prior rounds.)

- Knowledge-base entries to use / certified lemmas to import verbatim (no
  new proof needed, only p=19 substitution):
  - `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`
    (Generalized K_0-Boundedness + gcd-difference Witness Lemma)
  - `lemmas/legendre-sieve-gap-bound.md` (Legendre Sieve Gap Bound)
  - `lemmas/primorial-floor-bound.md` (Primorial Floor Bound)
  - `lemmas/universal-look-back-witness-identity.md` (r=1 corollary, and the
    general closed-form `c(p,j,r)` machinery from `a1-pq-subfamily-theorem`'s
    round-28 build, not yet promoted to its own lemma file but usable)
  - `lemmas/diagonal-characterization-and-first-risk-theorem.md`
    (`s_0(j,r)=1 <=> j=r`; First-Risk Theorem — both apply unchanged at
    p=19 and correctly predict all 7 exceptions land on the diagonal)
  - `approaches/a1-pq-subfamily-theorem.md` for the full symbolic §0-§8
    template to copy structurally (as a1-17q's builder did for a1-11q).

- Analogous past problems (cruxes): none of the crux corpus's pre-2026
  problems are close analogues of this bespoke greedy-gcd machinery (checked
  in prior rounds per current.md's own notes on aimo-1000 as the closest
  crux for H1/FAH, unrelated to this pq-subfamily computation); no new
  crux search was warranted for this narrow lens (pure computation +
  reuse of in-workspace certified machinery, not a fresh proof technique).

- Prior progress: 10 pq-subfamily theorems solved so far (p=3 [+3a,3q^2,3q^3
  variants], 5, 7, 11, 13, 17), all following the identical template. The
  general `a1-pq-subfamily-theorem` remains `partial` (uniform-in-p symbolic
  machinery proved; per-p Bad(p) computation and the diagonal-only Minimal-
  Window-Necessity conjecture remain open in general). p=19 is a completely
  routine next instance — no blocker found.

- Dead ends (do not retry): none new. Reconfirming prior workspace rules:
  do not use "exists i" legality semantics (must be gcd>1 against ALL prior
  terms) — verified my own simulator uses the correct "for all i" rule and
  cross-checked against the a1-17q file's independently-stated exceptions'
  exact deviation values as a sanity check of methodology (not literally
  re-run, but the pattern — diagonal band, K_0=p+1, window-emptiness —
  matches exactly).

- Small-case / intuition notes (Bad(19) computation — CONJECTURE, verified
  numerically, not yet a certified proof):
  - Ran the literal greedy-sequence simulation (correct "for all i" legality
    rule) for a1=19*q for every prime q in (19,20000), 2254 primes, 40 terms
    each.
  - **Bad(19) = {23, 29, 31, 37, 43, 53, 73}** — exactly 7 primes, zero
    additional deviations found up to q=20000 (535/542 matched in an initial
    q<4000 sweep, then 2247/2254 matched in the extended q<20000 sweep, same
    7 exceptions both times — stable).
  - Every exception is diagonal (deviation band `j` equals `r=q mod 19`
    exactly): (q,r) pairs are (23,4),(29,10),(31,12),(37,18),(43,5),(53,15),
    (73,16) — matching prediction from the certified Diagonal Characterization
    Lemma (`s_0(j,r)=1 <=> j=r`) and First-Risk Theorem.
  - All 7 have K_0 = 19+1 = 20 exactly (verified: deviation value / q = 20 in
    every case) — matching the Generalized K_0-Boundedness Lemma's
    diagonal-cell prediction `K_0=p+s_0=p+1`.
  - Elementary explanation for all 7 (opening 2 above, independently derived
    and checked this round): q=23,29,31,37 have window length 1 (single
    element q+1, always even, shares factor 2 with K_0=20 — automatic
    failure, no computation needed); q=43,53 have window length 2
    ({q+1,q+2}: q+1 even, q+2 ≡0 mod 5 in both cases — 45=9·5, 55=11·5);
    q=73 has window length 3 ({74,75,76}: 74 even, 75=3·5^2, 76 even) — all
    share a factor with 20.
  - No new obstruction type at p=19: |Bad(19)|=7 sits between |Bad(13)|=4 and
    |Bad(17)|=8 (non-monotonic in p, consistent with the already-noted
    non-monotonic pattern in `a1-pq-subfamily-theorem`'s open-gaps section,
    e.g. 2,2,3,6,7,10,12,... for p=3,7,5,11,13,17,19). K_0=p+1=20=2^2·5 has
    2 distinct prime factors, structurally the same situation as p=11
    (K_0=12=2^2·3), p=13 (K_0=14=2·7), p=17 (K_0=18=2·3^2) — no qualitative
    novelty. Table size for p=19 is (p-2)(p-1)=17·18=306 cells (largest yet,
    but a routine linear scale-up of the a1-17q build's 240-cell table).
  - r=1 column: none of the 7 Bad(19) primes has r=1 (residues found are
    4,10,12,18,5,15,16), consistent with the certified Universal Look-Back
    Witness Identity's r=1 corollary giving unconditional k=0 closure for
    that column — no counterexample.
  - This is all conjecture-strength evidence (numerical, to q=20000) for the
    *existence and exact membership* of Bad(19); the certified machinery
    (Legendre-Sieve + Primorial-Floor threshold argument, exactly as in
    a1-11q/13q/17q) is what would turn this into a proof, and per 6/6 prior
    instantiations at p=3..17 it is expected to succeed with no new
    obstruction. Build-readiness assessment: **ready**, purely a mechanical
    scale-up; no structural surprise found.

- H1 (FAH) / H2 (absorption-chain termination) note (brief, as instructed):
  current.md confirms a 23rd consecutive plateau round (rounds 6-29) on
  both H1 and H2 for the fully general Master Conditional Theorem. Nothing
  new surfaced from this lens's reading — this round's work is entirely
  orthogonal to H1/H2 (it only advances small-prime subfamily coverage, as
  the last 6 rounds' APPROVEs have done). No fresh idea to report on H1/H2
  from this pass; if the outliner wants to break the plateau, the strongest
  lever visible in the workspace remains the still-open Minimal-Window
  Necessity Conjecture (opening 3 above) — which is a genuinely different,
  general-p question, not yet another single-p instance, and could in
  principle also feed back into making the H1/H2-level argument's "generic
  seed" case more tractable if it generalizes beyond the pq family (untested
  speculation, not verified this round).
