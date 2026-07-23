# Lemma REC (Recursive IN/OUT Characterization)

**Source.** `approaches/similarity-dichotomy-crux-adaptation.md` (Round 15,
Section 1). Proved entirely from scratch from the problem's own recursive
definition — no external citation.

**Setup.** Fix the sequence `(a_n)_{n\ge1}` as in the problem (each `a_n>1`,
`a_1` fixed, `a_{n+1}` = smallest integer `>a_n` with `\gcd(a_{n+1},a_i)>1`
for all `1\le i\le n`). Write `k:=a_1`. Call an integer `n\ge k` a **term**
if `n=a_j` for some `j\ge1`, and a **non-term** otherwise (integers `<k` are
not classified).

**Statement.** Let `n>k` be an integer. Then `n` is a non-term if and only
if there exists a term `m` with `k\le m<n` and `\gcd(m,n)=1`.

**Proof.**

(⇐) Suppose some term `m` satisfies `k\le m<n` and `\gcd(m,n)=1`. If `n`
were itself a term, `n=a_j`, then since `m<n=a_j` is a term of the strictly
increasing sequence, `m=a_i` for some `i<j`. By the recursive definition,
`a_j` satisfies `\gcd(a_j,a_l)>1` for every `l=1,\dots,j-1`; taking `l=i`
gives `\gcd(m,n)>1`, contradicting `\gcd(m,n)=1`. Hence `n` is a non-term.

(⇒) Suppose `n>k` is a non-term. Since `(a_i)` is strictly increasing (hence
unbounded) and `a_1=k<n`, the set `\{i:a_i<n\}` is finite and nonempty; let
`j` be its maximum, so `a_j<n` and (by maximality) `a_{j+1}\ge n`. Since `n`
is not a term, `a_{j+1}\ne n`, so `a_{j+1}>n`, giving `a_j<n<a_{j+1}`. Since
`a_{j+1}` is by definition the **smallest** integer `>a_j` satisfying
`\gcd(\cdot,a_i)>1` for all `i\le j`, and `n` is a strictly smaller
candidate than `a_{j+1}`, `n` must fail that condition: some `i\le j` has
`\gcd(n,a_i)=1`. Set `m:=a_i`; then `m` is a term, `k\le m\le a_j<n`, and
`\gcd(m,n)=1`, as required. `∎`

**Certification.** Sorry-free, no gaps, elementary strong-induction-style
argument directly from the problem's own recursive rule. Fully
independently re-verified (fresh generator, random-sample stress test on
`a_1\in\{247,2747,21528751\}`, thousands of `n` each, zero violations,
round-15 proof-reviewer).
