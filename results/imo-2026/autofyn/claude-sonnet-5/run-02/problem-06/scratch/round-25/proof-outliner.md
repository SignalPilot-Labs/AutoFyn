## imo-2026-06

a1-3qk-subfamily-theorem: advance
Target: the approach's stated whole target is the general family a_1=3q^m
(all fixed m>=1) with literal T=1,L=3 periodicity from n=1, outside a finite
m-dependent exceptional set of primes q. This round's concrete milestone
(matching the precedent set when m=2 was closed and certified as its own
standalone theorem while the parent approach stayed `partial`) is: **close
m=3 completely**, producing a second standalone certified corollary
`a_1=3q^3` theorem, while leaving m>=4 as the still-open parent-approach gap.
Technique: identical two-branch Legendre-Sieve-Gap-Bound + Primorial-Floor-
Bound template already certified and used for m=1,2 (`lemmas/legendre-sieve-
gap-bound.md`, `lemmas/primorial-floor-bound.md`), re-derived with the
correct m=3 growth rates — NOT a new technique, a bookkeeping-heavy
re-derivation with new constants (per this round's m3-closure explorer,
which found the residual table stays small and finite — 12 exceptions at
k=0, all q<=479; 14 more at k>=1, all q<=71,k<=7 — a routine closure, not a
regime change; current.md's own "may need a genuinely two-dimensional
argument" speculation is explicitly NOT supported by the numerics and should
be retracted in the same edit that closes the gap).
Skeleton:
  1. Import Parts I-III verbatim (already certified m-generic: base case,
     a_n+1 illegality, odd-n Parity Witness, n_0/K_0(q,3)=3q^2+s_0 formulas)
     — by `lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`.
  2. Part IV, k=0 band, m=3: redo Claim 1 (the "auto" branch for r=omega(K_0)
     large) with the corrected order-of-magnitude relation K_0~3q^2
     (quadratic) vs L~q/3 (linear) — by a re-fitted Primorial-Floor-Bound
     corollary `(r+1)! >= C'*2^r(r+1)+D'` with new constants C',D' suited to
     this K_0/L ratio; the key subtlety (flagged by the explorer) is that
     because q ~ sqrt((s+1)!) here (vs q ~ (s+1)! at m=2), a WIDER range of
     small s must be checked directly as the induction's base case before
     the asymptotic branch is safe — this is the one genuinely new piece of
     work, not present at m=1,2.
  3. Part IV, k=0 band, small-r branch: generic bound 2^r(r+1) for r below
     the threshold from step 2, giving an explicit finite q-threshold;
     verify the resulting residual list against the 12 explicit numeric
     exceptions (all q<=479) via direct witness (mostly i=3, one i=4 at
     q=61) — by `gcd` computation, matching the m3-closure explorer's table
     exactly.
  4. Part IV, k>=1 band, m=3: same B0/B1/B2 structure as the certified m=2
     closure (`lemmas/a1-3q-squared-periodicity-theorem.md`), re-derived
     with m=3's K_0; verify the 14 explicit numeric exceptions (all q<=71,
     k<=7) via direct witness — by `gcd` computation.
  5. Assemble: Theorem (a_1=3q^3 literal periodicity) — for every prime
     q>=7,q!=5: a_n=3(q^3+n-1) for all n>=1. State and verify explicitly
     (T=1,L=3, substitute n=1 to recover a_1=3q^3) per the rigor rules.
  6. Correct current.md's speculative "k*~q^{m-2} two-dimensional" paragraph
     in the same edit — it is refuted by this round's own numerics (max
     failing k stays bounded at 7 for m=3, not growing with q).
Key lemmas (claim + mechanism):
  - Sharpened Primorial Floor Bound for K_0~q^2 — because r=omega(K_0)=s
    forces K_0>=(s+1)! (unchanged mechanism from the certified bound), but
    now K_0~3q^2 means the threshold q at which s first becomes reachable
    is q~sqrt((s+1)!) rather than q~(s+1)!, requiring the induction's base
    case to explicitly re-verify a wider band of small s before the
    "L~q/3 beats 2^r(r+1)" asymptotic argument is licensed.
  - Residual-table finiteness for m=3 — because the same Legendre sieve
    gap bound g(M)<=2^omega(M)(omega(M)+1) applies to any modulus M=K or
    qK regardless of how K_0 grows in q; only the CONSTANTS in the
    threshold derivation change with the K_0/L growth-rate ratio, not the
    finiteness conclusion itself.
Open gaps: the sharpened base-case verification (step 2) and the two
residual-table closures (steps 3-4) are unproved by this outline — they are
the builder's task, following the m=2 closure's exact template with new
constants. The analytic proof that NO further residuals exist beyond
q=479 (k=0) / q=71,k<=7 (k>=1) is required (not just the numeric scan to
q=60000/20000) — the builder must derive this from the sharpened Claim 1/2
thresholds, not merely cite the numeric scan as a proof.
Cases to cover: k=0 band (A); k>=1 band, split as needed into sub-bands
analogous to m=2's B0/B1/B2 (small-K generic bound vs large-K auto branch).
Watch out for: do not let the builder assume the m=2 constants (`(r+1)! >=
9*2^r(r+1)+8`) transplant unchanged — they must be re-derived for the new
K_0~q^2 growth rate; the residual table sizes (12+14=26) found numerically
are strong evidence but NOT a substitute for the analytic upper-threshold
proof required for a `solved` verdict, exactly as for m=1,2.

a1-5q-subfamily-theorem: advance
Target: for a_1=5q, prime q>=7, q not in {7,13,19}, literal T=1,L=5
periodicity from n=1: a_n=5q+5(n-1) for all n>=1.
Technique: identical strong-induction skeleton to the certified a_1=3q
theorem, generalized from one intermediate residual band (j=2) to three
(j=2,3,4), using the certified Legendre Sieve Gap Bound + Primorial Floor
Bound per band. Already outlined in the existing approach file with a
pre-build numeric check (round 23, outline-reviewer) confirming the exact
exceptional set {7,13,19} up to q<300 (recommend the builder extend this
sweep to q<3000 first, per this round's diversity-scout explorer, which
already ran exactly that extension and found no further exceptions).
Skeleton (already in the file, restated):
  1. a_n+1 illegal — unchanged, consecutive-integer coprimality.
  2. For each j in {2,3,4}: 5 does not divide a_n+j (since 5|a_n and
     j not congruent 0 mod 5); a_n+j illegal via i=1 whenever q does not
     divide a_n+j (Case (a)).
  3. Residual Case (b), q|(a_n+j): generalize the certified Parity/gcd-
     difference Witness identity gcd(N,a_n)=gcd(N,N-a_n)=gcd(N,j)
     (N:=a_n+j) — by the identity gcd(x,y)=gcd(x,x-y); derive, separately
     for each j in {2,3,4}, the exact residue condition on n making
     gcd(N,j)=1 (free witness i=n).
  4. Remaining gcd(N,j)>1 sub-cases: apply the certified Legendre Sieve Gap
     Bound / Primorial Floor Bound per (j,K) pair exactly as in the a_1=3q
     and a_1=3q^2 closures, producing a finite residual (k,K_0)-table per
     band j, resolved by explicit witness.
  5. Assemble: a_n+5 legal (shared factor 5) is forced only once ALL THREE
     bands j=2,3,4 are shown illegal for the relevant n.
  6. Confirm q in {7,13,19} are genuine structural exclusions (not
     resolvable, analogous to the certified q=5 exclusion mechanism in
     a1-3q) — derive explicitly why each of the three collides (expected:
     a small-window/no-witness collision in one of the three bands,
     mirroring the a1-3q q=5 mechanism's "candidate window always fails"
     argument).
Key lemmas (claim + mechanism):
  - Generalized Parity/gcd Witness (j-parametrized) — gcd(a_n+j,a_n)=
    gcd(a_n+j,j) for any offset j, by the same gcd(x,y)=gcd(x,x-y)
    identity already certified for j=2; genuinely new content is the
    per-j, per-band residue characterization.
  - {7,13,19} exclusion mechanism — because in at least one band j, the
    admissible witness window is empty for exactly these three q (needs
    an explicit small-window computation analogous to a1-3q's q=5 case,
    where the sole candidate parity fails).
Open gaps: steps 3-6 (full triple-band closure) are the builder's task;
the exclusion mechanism for {7,13,19} (step 6) needs an explicit proof,
not just numeric confirmation.
Cases to cover: j in {2,3,4} x (Case a / Case b) x (k=0 / k>=1 residual
band per j) — roughly 3x the casework of the certified a1-3q closure.
Watch out for: builder should extend the pre-build sweep to q<3000 (already
done by this round's diversity-scout explorer, zero new exceptions found)
before investing in the general proof, to avoid the a1-3qk m>=2 mistake of
under-scanning before committing to a threshold derivation.

a1-pq-subfamily-theorem: new
Target: a genuinely broader claim than any single-prime-pair subfamily so
far — for EVERY fixed odd prime p (not just p=3 or p=5), there is an
explicit finite exceptional set Bad(p) of primes q such that for a_1=p*q,
q prime, q not in Bad(p) union {p}, literal T=1,L=p periodicity holds from
n=1: a_n=pq+p(n-1) for all n>=1. This subsumes the certified a1-3q theorem
(p=3, Bad(3)=empty beyond the q=5 structural exclusion) and the (pending)
a1-5q theorem (p=5, Bad(5)={7,13,19}) as explicit corollaries, and is a
genuinely new top-level target (a claim about ALL prime pairs at once, not
one more single-p instance) per this round's diversity-scout explorer, which
found the underlying sieve mechanism (Legendre Sieve Gap Bound + Primorial
Floor Bound + generalized parity/gcd-difference witness) never actually used
p=3 specifically anywhere in its certified proof, and verified numerically
for p in {5,7,11,13,17,19,23,29,31,37,41,47} that each gives a finite,
range-stable (checked to 3x range for p=29,41) exceptional set.
IMPORTANT CORRECTION TO A RECORDED DEAD END: round 19's memory-rule-23
"a_1=p*q definitively refuted" finding pre-dates the Legendre Sieve Gap
Bound/Primorial Floor Bound (both certified round 22) and only refutes
searching for a NAIVE CLOSED-FORM threshold rule (e.g. q>=2p) directly from
raw numerics — it does not and cannot rule out a sieve-toolkit-based proof,
which did not exist yet at round 19. This approach is not a re-proposal of
the dead-end; it targets the toolkit-based route, explicitly distinguished.
Technique: Direct strong induction, technique identical to a1-3q/a1-5q but
with p-1-2=p-3... (p-2 intermediate bands j=2,...,p-1), each closed by the
same Legendre Sieve Gap Bound / Primorial Floor Bound / generalized
parity-witness toolkit — NOT a new technique, a genuinely new SCOPE
(uniform in p, not fixed p).
Skeleton:
  1. a_n+1 illegal — unchanged, p-independent, consecutive-integer
     coprimality (by Free Facts Lemma).
  2. For each j in {2,...,p-1}: p does not divide a_n+j (since p|a_n by IH
     and j not congruent 0 mod p, as 1<=j<=p-1); a_n+j illegal via i=1
     whenever q does not divide a_n+j (Case (a), p-independent).
  3. Residual Case (b), q|(a_n+j): the generalized gcd-difference witness
     identity gcd(N,a_n)=gcd(N,j) (N:=a_n+j) is already p-independent (only
     depends on j); when gcd(N,j)=1, witness i=n is free. Characterize, for
     each fixed small j, the residue condition on n (this depends only on
     j's own factorization, e.g. j even vs odd vs composite — NOT on p
     beyond j<p).
  4. Remaining gcd(N,j)>1 sub-cases: apply the certified sieve toolkit per
     (j,K) pair, exactly as in a1-3q/a1-5q/a1-3q^2, producing a finite
     residual q-set per band j. THE KEY OPEN QUESTION (new, not yet
     attempted anywhere): does the resulting per-band threshold derivation
     (Claim 1/Claim 2 style) go through UNIFORMLY in p, i.e. can the
     builder write ONE inequality chain with p as a free parameter, or does
     each p genuinely require its own constant-fitting (as m did for
     a1-3qk)? Given the growing exception counts observed numerically
     (2 at p=3,7; up to 26 at p=41), this is a real, unresolved uncertainty
     the builder must investigate FIRST as a cheap check (attempt the p=7
     case symbolically, treating p as a variable in the threshold algebra)
     before committing to a full general-p proof.
  5. Assemble: a_n+p legal (shared factor p) forced only once all p-2 bands
     j=2,...,p-1 are shown illegal.
  6. State the theorem at the achieved level of generality — EITHER (a) a
     single uniform-in-p statement (Bad(p) characterized by one p-parametric
     sieve-threshold formula), OR, if step 4's uniformity check fails, (b)
     a theorem schema ("for every fixed prime p, the same finite-closure
     PROCEDURE applies, producing an explicit Bad(p)") with p=3,5 worked out
     as explicit certified corollaries (importing the already-certified
     a1-3q theorem and the a1-5q theorem once built) — (b) is an honest,
     acceptable fallback scope, NOT a failure, and should be stated as such
     if (a) does not close in one round.
Key lemmas (claim + mechanism):
  - p-Independence of Case (a)/(b) split — because the Free Facts and
    gcd-difference identities never reference p's specific value, only
    a_n's divisibility by p (guaranteed by the inductive hypothesis) and
    j's own arithmetic — a direct transplant, re-verify explicitly rather
    than assume (per the standing workspace rule about numeric-value vs
    prime-support transplants).
  - Growth of |Bad(p)| with p — because more bands (p-2 of them) mean more
    independent opportunities for a small-window collision (the
    a1-3q q=5 mechanism, generalized): NOT a sign of the technique failing,
    but of more casework, matching the numeric pattern (2,2,7,6,10,12,20,26
    exceptions for p=3,7,5,13,17,23,29,41 respectively per the explorer's
    scan — note p=3 and p=5 both have small counts, consistent with the
    unordered "count grows roughly with p" trend, not a hard threshold).
Open gaps: the entire step-4 uniformity question (does one threshold
argument work for all p, or must each p be separately constant-fitted) is
the central open gap — genuinely unknown, not yet attempted by anyone. The
per-j gcd(N,j)=1 residue characterization (step 3) for general j is also
unproved (only done for j=2 so far, in the certified a1-3q lemma).
Cases to cover: j in {2,...,p-1} (p-2 bands) x (Case a/b) x (k=0/k>=1)
per band — this is the largest casework any approach in this workspace has
attempted; the builder should explicitly budget effort: attempt uniformity
first, fall back to the p=3,5-corollary schema (option (b) above) if it
does not close within the round.
Watch out for: do not let the builder silently narrow to "just redo p=7 as
a fourth single-prime instance" and call that the general theorem — the
whole point of this approach's distinct scope is the UNIFORM-IN-p claim (or
the honestly-scoped schema fallback); a single new fixed-p instance
belongs in a1-5q's family, not here. Also watch for the m>=2-style trap:
verify (cheaply, numerically, before any general proof) that Bad(p) is
actually stable (does not grow) under a 3x range extension for at least 2-3
values of p, exactly as this round's explorer already did for p=29,41 —
do not skip this pre-build sanity check.

n1-periodicity-reconciliation: advance
Target: unchanged — the gap-free Master Conditional Theorem reducing the
fully general problem to H1 (FAH) and H2 (self-absorbing-core termination),
consolidated and audited each round; this round's task is a documentation
correction, not new positive content toward H1/H2 themselves.
Technique: consolidation/audit, as in prior rounds (n/a — no new proof
technique this round).
Skeleton:
  1. Fold in this round's H2-asymmetry explorer's corrected diagnosis of
     round 24's "a_1=11305 diverges ~sqrt(N)" finding: the GLOBAL power-law
     fit (contaminated by early transient growth) is retracted; the
     corrected LOCAL exponent analysis (consecutive-checkpoint fits) shows
     BOTH canonical hard seeds (a_1=4807, 11305) decelerating in their
     new-extended-type recruitment rate, just at different rates/scales —
     4807's exponent drops sharply (0.14 plateau -> 0.09 -> 0.06) between
     n=500k and n=1M, while 11305's drops more mildly (0.28 -> 0.22) and
     has not yet shown the late-stage collapse at its current frontier
     (n=750k) — by direct citation of this round's re-simulation (own SPF-
     sieve script, 4807 to n=1,000,000, 11305 to n=750,000, both
     cross-checked against round 24's numbers at shared checkpoints,
     exact match).
  2. State explicitly, per the corrected data: this round's evidence argues
     for "H2's existence hypothesis is plausible but numerically
     unconfirmed at 11305 due to insufficient runway (its Finite-Core-
     Theorem-enlarged core is 1/3 larger than 4807's, |S_0|=12 vs 9, giving
     an 8x larger nominal extended-type state space)" rather than round 24's
     more alarmed "may threaten H2" framing — a genuine walking-back of a
     prior round's overreading, matching the workspace's standing practice
     (round 20's H2 numeric-window-artifact correction is the closest
     precedent: do not treat a non-stabilizing window as evidence of
     non-termination without first checking a substantially larger window).
  3. Do NOT claim this constitutes evidence FOR H2 either — record it as a
     corrected-but-still-inconclusive numeric picture, and note the two
     concrete next steps an H2-attacking approach would need (either much
     deeper computational reach for 11305, past n~2-5M, or an actual
     structural/analytic bound on new-prime-recruitment rate, which the
     certified lemma stack still completely lacks per round 24's finding).
Key lemmas (claim + mechanism): none new — this is a documentation/audit
correction, not a new certified result.
Open gaps: H1 and H2 both remain fully open for the general problem; this
advance does not narrow either, it only corrects a mis-diagnosed numeric
signal from round 24 so future rounds don't waste effort chasing a
"disprove H2 via 11305" framing that the corrected data no longer supports.
Cases to cover: none (documentation only).
Watch out for: do not let this correction be read as new evidence FOR H2 —
it is strictly a retraction of an overly pessimistic prior reading, not a
positive result; keep the "H2 remains open, no lemma bounds recruitment
rate" honest framing explicit in the write-up, per the standing rule against
overclaiming (CLAUDE.md rigor rules: "Prove, don't conjecture").
