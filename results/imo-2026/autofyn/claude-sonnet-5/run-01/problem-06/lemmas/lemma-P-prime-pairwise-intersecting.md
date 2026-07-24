# Lemma P′ (pairwise global intersection)

**Statement.** With `(a_n)` as in the problem, for every `1\le i<j`, `\gcd(a_i,a_j)>1`.
Equivalently, writing `P_n:=\mathrm{rad}(a_n)` (the set of prime divisors of `a_n`),
the family `\{P_n\}_{n\ge1}` is **pairwise intersecting**: `P_i\cap P_j\ne\varnothing`
for all `i<j` (not merely for pairs involving index `1`, which is the content of the
weaker Lemma P).

**Proof.** `a_j` (for `j\ge2`) is `a_{(j-1)+1}`, chosen subject to `\gcd(a_j,a_m)>1`
for every `m=1,\dots,j-1`. Since `i\le j-1`, taking `m=i` gives `\gcd(a_i,a_j)>1`.
$\blacksquare$

**Source.** Proved as "Lemma P′" in `approaches/backbone-existence-crt.md` (Section 1)
and, independently, inline (unnamed but identical) inside the proof of "Lemma R" in
`approaches/intersecting-family-covering-construction.md`. Both derivations are the
same one-line argument from the problem's own recursive definition.

**Certification.** No hypotheses beyond the problem's own definition; no gaps;
elementary. Strictly stronger than Lemma P (recovers it by setting `i=1`). Certified
`solved`-quality (sorry-free) by the round-1 proof-reviewer. This is the correct
formal justification behind the "eternal witness" pigeonhole argument (Lemma R) and
behind Lemma 1's proof (both currently invoke the `i<j` case, i.e. genuinely need
Lemma P′, not just Lemma P, when `i\ge2`).
