# Interleaving/Periodicity Theorem (resolves the whole problem)

**Source.** `approaches/similarity-dichotomy-crux-adaptation.md` (Round 15,
Section 7). New content beyond the crux (`aimo-0030`'s official solution
only needs the Dichotomy Theorem itself; its Comment 3 only sketches
"the period divides `P`" without a full proof). This theorem gives a
complete, self-contained, **exact** (not eventual) periodicity proof from
`n=1`, citing only the already-certified Main Dichotomy Theorem
(`lemmas/theorem-similarity-dichotomy.md`).

**Statement.** Let `(a_n)_{n\ge1}` satisfy the problem's hypotheses, let
`k:=a_1`, and let `L:=P:=\prod_{p\le k\text{ prime}}p` (finite). Let
`T:=\#\{r\in\{0,\dots,P-1\}: \text{every }n\ge k\text{ with }n\equiv r
\pmod P\text{ is a term}\}` ("good residues"). Then `1\le T\le P`, and
`a_{n+T}=a_n+L` for **every** positive integer `n`.

**Proof.**

*Step 1.* If `n\equiv n'\pmod P` (both `\ge k`), then for every prime
`p\le k` (so `p\mid P`), `n\equiv n'\pmod p`, hence `p\mid n\iff p\mid n'`;
so `\sigma(n)=\sigma(n')`, i.e. `n,n'` are similar. By the Main Dichotomy
Theorem, they have the same term-status. So every residue class mod `P`
(among integers `\ge k`) is uniformly "good" (all terms) or "bad" (all
non-terms).

*Step 2.* Hence `\{n\ge k: n\text{ term}\}=\{n\ge k: n\bmod P\text{ good}\}`
(⊆ is immediate; ⊇ is Step 1). Since `k=a_1` is always a term, `k\bmod P`
is good, so `T\ge1`; trivially `T\le P`.

*Step 3.* List the `T` good residues; let `\beta_1<\cdots<\beta_T` be their
unique representatives in `[k,k+P)` (a complete residue system mod `P`).
Since `k`'s residue is good and `k$ is the least possible value `\ge k`
attainable, `\beta_1=k`.

*Step 4 (interleaving).* By Step 2, the full term set (all `\ge k`) is
`\bigcup_{l=1}^T\{\beta_l+jP:j\ge0\}`. Sorting this union: within a fixed
"block" `j`, the `T` values `\beta_1+jP<\cdots<\beta_T+jP` are already
sorted; and `\beta_T+jP<\beta_1+(j+1)P` since `\beta_T-\beta_1<P` (both lie
in the length-`P` interval `[k,k+P)`). So blocks are totally ordered and
the sorted enumeration `g_1<g_2<\cdots` of the union satisfies
`g_{mT+l}=\beta_l+mP` for every `m\ge0`, `l\in\{1,\dots,T\}`.

*Step 5.* Hence for every `n\ge1`, writing `n=mT+l` (`1\le l\le T$):
`g_{n+T}=g_{(m+1)T+l}=\beta_l+(m+1)P=g_n+P`.

*Step 6.* Since `(a_n)_{n\ge1}` is, by definition, the strictly increasing
enumeration of the term set (each `a_n` a term, every term equal to some
`a_n`), and this set equals (Step 2) the explicit union just enumerated,
uniqueness of the increasing enumeration of a set gives `g_n=a_n` for
every `n\ge1`.

**Conclusion.** `a_{n+T}=a_n+P=a_n+L` for every `n\ge1`, with `L=P` and
`1\le T\le P` both finite positive integers explicitly described above.
This is exactly the conclusion the problem asks for. `∎`

**Certification.** Sorry-free; cites only the already-certified Main
Dichotomy Theorem plus elementary facts about complete residue systems
and merging arithmetic progressions with a common difference. Not
claimed to give the *minimal* period (it need not be minimal — e.g. for
`a_1=15`, the formula gives `(T,L)=(8008,30030)=1001\cdot(8,30)`, a
genuine but non-minimal multiple of this workspace's independently
certified minimal period `(8,30)`; the problem only asks for existence of
*some* `T,L`, which this supplies). Independently re-verified by the
round-15 proof-reviewer: fresh-code exact reproduction of the periodicity
table for `a_1\in\{2,3,4,5,6,7,9,10,11,12,14,15\}` (12 values, 8 of them
new relative to the builder's own test set), zero exceptions across
thousands of checked indices per value.
