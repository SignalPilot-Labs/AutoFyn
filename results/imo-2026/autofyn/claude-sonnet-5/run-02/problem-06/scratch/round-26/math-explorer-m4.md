## imo-2026-06 (lens: a1-3qk-subfamily-theorem, extend m=3 -> m=4)

- Distinct openings:
  1. Attempt to close m=4 exactly as m=1,2,3 were closed (same Legendre
     Sieve Gap Bound + Primorial Floor Bound template, refit constants).
     **This round's numerics show this does NOT work as a routine repeat** —
     see below. Any outline pursuing this must explicitly address the two
     new obstacles found.
  2. Treat m=4 (and beyond) as requiring an *excluded-exceptional-prime*
     framing analogous to the certified q=5 exclusion in the base a1-3q
     theorem, i.e. state the theorem as "for every prime q>=7, q not in a
     small excluded set E_4" and separately, honestly, leave E_4's members
     open (not attempt to resolve them within this approach).
  3. Abandon the fixed-m generalization axis at m=4 and instead pursue the
     `a1-pq` approach's "uniform machinery, per-value finite table" framing
     one level up: try to find a uniform-in-m argument for the k=0 branch
     that avoids the (m-1)-th-root-of-factorial blowup (see obstacle 2
     below) rather than doing per-m ad hoc constant-refitting forever.

- Candidate technique(s): same certified toolkit (Legendre Sieve Gap Bound,
  Primorial Floor Bound, the m=3 "OR-split" device for k>=1) — but the
  toolkit's naive translation from m=3 to m=4 produces an intractable
  analytic threshold (obstacle 2) and the underlying claim is not even true
  as stated (obstacle 1). Do NOT dispatch a builder expecting a routine
  "bigger table, same difficulty" close.

- Cheap-kill candidates: for k=0, the residual band is exactly determined
  by the certified `omega(K_0)` sieve criterion — a witness fails to exist
  only when the crude bound `L >= 2^r(r+1)` fails AND no small-i witness
  happens to work; this is checkable with a fast (~seconds) sympy scan per
  q, no heavy computation needed to find candidates, only to confirm
  witness existence in each flagged case.

- Knowledge-base entries to use: the same `lemmas/legendre-sieve-gap-bound.md`
  and `lemmas/primorial-floor-bound.md` used for m=1,2,3; no new KB entries
  found needed or available (per round 21/24/25 notes, no Jacobsthal-type
  citable literature bound exists in KB/crux corpus).

- Analogous past problems (cruxes): none new found this lens — this is
  pure continuation of already-imported machinery, not a fresh corpus
  search. (Prior rounds already established no better off-the-shelf sieve
  tool exists; not re-litigated here.)

- Prior progress: `current.md` / `a1-3qk-subfamily-theorem.md` fully closes
  m=1,2,3 (certified). Its own "Open gap" section for m>=4 flags two
  *anticipated* obstacles (threshold constants grow with m; the OR-split's
  exponent-matching needs re-derivation per m) but explicitly says these
  were "not verified for m>=4" and treats the round-25 explorer's m=4,5
  spot check (q<1500, k-band only, no k=0 residual list actually computed)
  as "supporting" a conjecture that the template closes every m. **This
  round's deeper numeric work shows that conjecture is WRONG as stated for
  m=4** (see below) — the m=4 case is qualitatively, not just
  quantitatively, harder.

- Dead ends (do not retry): none newly found dead this round; rather a
  positive claim in current.md ("reasonable to CONJECTURE the template
  closes every m") needs correction/qualification per the findings below.

- Small-case / intuition notes (all this round's own numeric work, own
  sympy/python scripts, `/tmp/m4explore/`):

  **Finding 1 — genuine counterexample at m=4, q=17, k=0 (NOT a search
  artifact).** Ran the same k=0/k>=1 crude-sieve-bound scan used to close
  m=1,2,3, now for m=4, up to q<500,000 for k=0 (kmax=2) and q<3000 with
  kmax up to 60 (also q<50000,kmax=15). The list of primes where the crude
  bound `L >= 2^omega(K)(omega(K)+1)` fails stabilizes at exactly **19**
  k=0 instances (q in {11,13,17,23,29,31,47,59,83,89,97,107,131,137,167,
  197,227,347,419}, all <=419) and **28** k>=1 instances (all q<=173,k<=12) —
  comparable in size progression to m=1 (18), m=2 (9), m=3 (26): 47 total,
  consistent with the "table grows mildly with m" pattern. For 46 of these
  47, an explicit small-i witness (i in {2,3,4,5,7}) was found by direct
  search, exactly matching the m=1,2,3 pattern. **But for q=17, k=0
  (n_0=6, K_0=14740, window L=5), NO witness exists in the required range
  i=2,...,6** — verified by exhaustive check of every i in that window.
  This is not an under-search: direct literal-greedy-recursion simulation
  of a_1=3*17^4=250563 confirms the sequence genuinely deviates at n=7:
  the "should-be-illegal" candidate a_6+2=250580=2^2*5*11*17*67 is in fact
  LEGAL (shares a prime factor with every one of a_1,...,a_6: 17|a_1,
  2|a_2, 11|a_3, 4=2^2|a_4, 5|a_5, 2|a_6 — confirmed by direct gcd/
  factorint computation), so a_7=250580 (gap 2, not 3), breaking the
  Case-(b) argument outright — the theorem's literal conclusion is FALSE
  for q=17 as stated. Extending the simulation to n=60 shows the gap
  sequence does NOT resettle to a constant-3 pattern (gaps alternate
  3,3,3,3,3,2,4,6,6,6,3,3,6,6,6,6,3,3,6,3,3,6,6,3,3,6,6,6,6,... through
  n=60) — so this is not even "T=1,L=3 eventually, just not from n=1";
  whatever periodicity this instance eventually has (if any, per the
  general unproved FAH/H2 machinery) is not visible in a simple form at
  this scale. **Conjecture, not proof: q=17 may be the only exception (no
  other witnessless case found up to the tested ranges), but this is
  unverified — a second, third, ... exception at larger q cannot be ruled
  out from this round's search alone.**

  **Finding 2 — the naive threshold-scaling makes the m=1,2,3
  "exhaustive-computation" closure step computationally intractable at
  m=4, independent of Finding 1.** Following exactly the m=3 Claim-1
  derivation pattern (cube-root generalization of the square-root relation
  used there), the k=0 branch's base-case threshold for "generic bound
  handles all remaining r" comes out at `r_0(4) ~= 30` (found by direct
  search of `(r+1)! >= 3*(3*2^r(r+1)+2)^3`, true first at r=30, vs m=3's
  r_0=15). This gives a *theoretical* sufficient q-threshold above which
  the sieve bound holds unconditionally of roughly `q >= 3*2^30*31+2 ~
  2*10^11` — i.e., to reproduce m=3's proof shape ("exhaustively verify
  every prime below the threshold, ~59,321 primes at m=3, seconds of
  compute"), m=4 would require exhaustively verifying primes up to
  ~2*10^11, many orders of magnitude beyond feasible brute-force
  computation (m=3's threshold, 737,282, was tractable; m=4's naive
  translation is not). The empirical residual band (stable to q<500,000,
  size 19) is almost certainly the TRUE exceptional set, but *proving*
  that rigorously via the same method needs either (a) a genuinely sharper
  inequality bringing r_0(4) down substantially (not attempted this round),
  or (b) a fundamentally different, non-exhaustive argument for why no
  further failures occur beyond a moderate q (e.g. an explicit uniform
  witness construction, bypassing the sieve-existence argument entirely).
  Neither is in hand.

  **Assessment for the outliner: m=4 is NOT a routine repeat of the m=3
  pattern.** It differs structurally in two independent ways: a genuine
  counterexample (Finding 1, requiring careful exceptional-set handling,
  open whether finite or how large) and a computationally-intractable
  naive threshold (Finding 2, requiring new analytic sharpening, not just
  "bigger numbers, same effort"). **Not ready for a proof-outliner to build
  a closeable m=4 outline this round as a straightforward extension.** If
  pursued at all, the outline must (i) explicitly carve out q=17 (and
  possibly search harder for further exceptions before claiming a clean
  finite excluded set, mirroring the q=5 precedent but with unknown final
  size), and (ii) either derive a substantially sharper k=0 threshold
  inequality than the naive cube generalization, or find a different
  (non-sieve-existence) argument for the k=0 large-q regime. Given the
  budget most rounds have spent per m (multiple builds each for m=1,2,3),
  a full m=4 closure attempt this round is high-risk; consider whether the
  `a1-pq`-style "uniform machinery, defer literal exceptional-set
  pinning" framing, or simply stopping the fixed-m generalization axis at
  m=3 (already 3 certified instances, a defensible floor deliverable) and
  redirecting effort elsewhere (H1/H2), is the better use of a build slot
  this round.
