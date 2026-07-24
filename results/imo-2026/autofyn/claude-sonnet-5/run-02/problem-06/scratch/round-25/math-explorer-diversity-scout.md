## imo-2026-06 (lens: diversity scout — next tractable a_1-subfamily, general-p*q axis)

- Distinct openings:
  1. **BIGGEST FINDING: `a_1 = p*q` generalizes cleanly to EVERY small fixed
     prime `p` (not just `p=3,5,7,11`) — a genuinely new, much larger unifying
     subfamily target, using the EXISTING certified toolkit unmodified.**
     Numerically verified (own `math.gcd`-based simulator, `math.gcd` per
     memory rule 13/26, sanity-checked against known a_1=15 sequence) for
     `p in {5,7,11,13,17,19,23,29,31,37,41,47}`, sweeping `q` prime up to
     1000 (and re-swept `p=29,41` up to `q<3000` to test for boundedness):
     every `p` tested gives a **finite, fixed exceptional set of `q`'s**
     (literal `T=1,L=p` periodicity `a_n=pq+p(n-1)` fails only at those
     `q`'s) that does **not grow** when the `q`-range is extended
     3x further (e.g. `p=29`: exactly the same 20 exceptional `q`'s at
     `q<1000` and `q<3000`; `p=41`: same 26 exceptional `q`'s at both
     ranges). This is the SAME qualitative shape as the certified `a1-3q`
     theorem (2 exceptions) and `a1-3^a q` theorem — just with more
     exceptions as `p` grows (`p=5`:3, `p=7`:2, `p=11`:7, `p=13`:6, `p=17`:10,
     `p=23`:12, `p=29`:20, `p=41`:26). The growth in exception count is
     exactly what the toolkit predicts: `p` fixed small forces checking
     `p-2` intermediate residue "bands" `j=2,...,p-1` (memory rule 19's
     observation), each needing its own Legendre-sieve residual-band
     closure, so casework scales with `p`, but the underlying mechanism
     (Parity/gcd-difference Witness `gcd(N,a_n)=gcd(N,N-a_n)` + Legendre
     Sieve Gap Bound + Primorial Floor Bound) is `p`-agnostic — it never
     used `p=3` specifically anywhere in its certified proof.
  2. **This appears to CONTRADICT round 19's memory rule 23/dead-end
     finding ("a_1=p*q DEFINITIVELY REFUTED... no monotone threshold")
     — but does not, once dated correctly.** Round 19 pre-dates the
     Legendre Sieve Gap Bound / Primorial Floor Bound (both first certified
     round 22). Round 19's negative finding was about searching for a
     SIMPLE closed-form threshold rule (e.g. `q>=2p`) directly from raw
     numerics, which genuinely doesn't exist (the exceptional sets above are
     not simple inequalities in `p,q` — e.g. `p=13`'s exceptions are
     `{7,11,17,19,23,47}`, no clean pattern). It was NOT a claim that no
     PROOF via the sieve-toolkit mechanism exists — that mechanism didn't
     exist yet. Recommend the outliner explicitly note this dating
     correction rather than treating memory rule 23 as a blanket veto on
     `p*q` (it correctly vetoes searching for a naive closed-form threshold,
     which is a different, narrower claim than "the sieve toolkit closes
     it").
  3. **Practical framing for a build: prove `a_1=3q` (done), `5q` (outline
     exists, `approaches/a1-5q-subfamily-theorem.md`, currently deprioritized/
     unbuilt), then EITHER (a) push `5q` to a 5th APPROVE as the cheapest
     next win (only 3 exceptions, 3 residue-bands `j=2,3,4` — the outline's
     own casework estimate), OR (b) attempt one general `a_1=pq` theorem
     for ALL odd primes `p<q` at once, stating the exceptional set as "a
     finite, `p`-dependent, sieve-derived set" rather than an explicit
     closed form — this would retroactively subsume `a1-3q`, `a1-5q`,
     `a1-7q`, etc. as corollaries at `p=3,5,7`.** Given CLAUDE.md's
     preference for genuinely distinct top-level targets over incremental
     technique variants, framing (b) (the general theorem) is the more
     valuable NEW subfamily to open this round; framing (a) is a safe,
     nearly-drafted fallback if (b) proves too casework-heavy in one round.
  4. Checked the "combined-axis" candidate `a_1=3^a*q^m` (both generalization
     axes at once) — as expected from the certified `K_0`-boundedness
     criterion (round 24), this is NOT tractable: `K_0` still grows with `q`
     for `m>=2` regardless of `a`, so it inherits `a1-3qk`'s `m>=2` failure
     mode. Not tested numerically (redundant with the already-certified
     algebraic reason); do not propose this combination.
  5. Checked `a_1 = p*q^m` for `p` fixed small, `m>=2` (i.e., the `q^m`-axis
     failure applied to bases other than 3) — same `K_0~p*q^{m-1}` growth
     problem as `a1-3qk`'s stuck `m>=2` case. Confirms the "large prime must
     stay to the first power" criterion (round 24 opening 2) is truly
     `p`-independent, not a `p=3`-specific artifact. Not a new opening.

- Candidate technique(s): the EXISTING certified toolkit only — Legendre
  Sieve Gap Bound (`lemmas/legendre-sieve-gap-bound.md`), Primorial Floor
  Bound (`lemmas/primorial-floor-bound.md`), the Parity/gcd-difference
  Witness identity `gcd(N,a_n)=gcd(N,N-a_n)` (used per-band, generalized in
  `a1-5q-subfamily-theorem.md`'s outline to `gcd(N,j)` for each intermediate
  offset `j`), and the Generalized Primorial Floor Corollary + corrected
  witness-window identity from `lemmas/a1-3aq-generalized-corollary-and-
  mechanisms.md` (reusable verbatim for the `K_0=p+O(1)` bookkeeping at
  general `p`). No new machinery needed.

- Cheap-kill candidates: the `K_0`-boundedness-as-`q→∞` pre-screen (round 24,
  confirmed again this round) — compute `K_0` symbolically for any proposed
  `a_1=f(q)` family and reject on sight if it grows with `q`. Also a new
  cheap check found this round: **before committing a build slot to a
  specific `p`, first numerically sweep `q` to `~3x` the intended proof
  range to confirm the exceptional set has actually stabilized** (as I did
  for `p=29,41` above) — this is a 30-second check that would have flagged
  `a1-3qk`'s `m>=2` growth problem even earlier had it been applied before
  round 23's build.

- Knowledge-base entries to use: none beyond the already-certified lemmas
  above (all already in `results/imo-2026-06/lemmas/`); `knowledge_base.md`'s
  generic sieve/pigeonhole/induction entries remain the relevant ones per
  prior rounds, no new KB entry found.

- Analogous past problems (cruxes): none newly found this round — this is a
  pure elementary-number-theory sieve/induction extension of already-mined
  workspace lemmas, not a corpus-retrieval question. (Round 24's diversity
  scout already exhaustively re-checked the crux corpus for this problem's
  H1/general framing and found nothing new; I did not re-run that search
  since my lens is subfamily scouting, where the relevant "corpus" is this
  workspace's own certified lemma library, already fully surveyed above.)

- Prior progress: 4 certified subfamily theorems (`2|a_1`; `a_1=p^k`;
  `a_1=3q`; `a_1=3^a q` for `a=1,...,5`) + certified standalone `a_1=3q^2`
  (housed in still-partial `a1-3qk-subfamily-theorem`) + gap-free Master
  Conditional Theorem (H1=FAH, H2=absorption-chain termination). `a1-5q-
  subfamily-theorem` exists as an unbuilt outline (round 23) with a
  pre-build numeric check already confirming its exact 3-exception claim
  (`q in {7,13,19}`) — matches my independent re-sweep exactly (`p=5`
  fails at `q=7,13,19` and nowhere else up to `q<1500`).

- Dead ends (do not retry):
  - `a_1=3^a*q^m` (combined both axes): dead on arrival via the certified
    `K_0`-boundedness criterion, `m>=2` inherits `a1-3qk`'s failure mode.
  - `a_1=p*q^m`, any fixed small `p`, `m>=2`: same failure mode, confirmed
    `p`-independent.
  - `a_1=c*q` with `c` a product of >=2 distinct odd primes (e.g. `15q,
    45q`): reconfirmed dead per round 24 (`|Q|>=3` FAH-hard regime).
  - Treating memory rule 23 ("`a_1=p*q` refuted") as a blanket veto on the
    sieve-toolkit route: this round's evidence shows that finding was about
    a pre-toolkit naive-threshold search (round 19), not the now-available
    Legendre-sieve mechanism — do not cite it as a reason to avoid a
    toolkit-based `a_1=pq` general theorem.

- Small-case / intuition notes (all CONJECTURE from numerics, not proofs):
  - For every tested prime `p in {5,7,11,13,17,19,23,29,31,37,41,47}`,
    `a_1=pq` (prime `q!=p`) shows literal `T=1,L=p` periodicity except a
    finite, `p`-dependent exceptional set of small `q`'s (verified stable
    under 3x range extension for `p=29,41`; verified up to `q<1000` for the
    rest). Exception count roughly grows with `p` (2 at `p=3`&`p=7`, up to
    26 at `p=41`), consistent with the `p-2`-intermediate-candidate-bands
    picture, not a sign of the mechanism breaking down.
  - No simple closed-form pattern in the exceptional `q`'s themselves was
    found (e.g. `p=13`: `{7,11,17,19,23,47}` — no obvious residue/inequality
    rule), consistent with round 19's finding that exceptions must be
    identified via the sieve/hand-check machinery, not guessed.
  - This suggests the most efficient round-25 build target is a **general
    `a_1=pq` theorem parametrized by `p`** (stating the sieve-derived
    finite exceptional set abstractly, with `p=3,5` worked out as explicit
    corollaries/sanity checks) rather than one-off `p`-by-`p` subfamily
    theorems — higher leverage per build slot than continuing the `a1-3qk`
    `m>=3` push or a 6th `a1-3aq` extension to `a>5`.
