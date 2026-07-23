# Lemma P (permanent hub)

**Statement.** Let `a_1,a_2,\dots` be the sequence defined in the problem (`a_1>1`,
and for every `n\ge1`, `a_{n+1}` is the least integer `>a_n` with `\gcd(a_{n+1},a_i)>1`
for every `i=1,\dots,n`). Then for every `n\ge2`, `\gcd(a_n,a_1)>1`.

**Proof.** By definition, `a_n` (for `n\ge2`) is `a_{(n-1)+1}`, chosen subject to
`\gcd(a_{(n-1)+1},a_i)>1` for every `i=1,\dots,n-1`. Since `n\ge2`, the index `i=1`
occurs among `1,\dots,n-1`, so in particular `\gcd(a_n,a_1)>1`. $\blacksquare$

**Source.** Proved identically (one line from the problem's own recursive definition)
in `approaches/backbone-existence-crt.md` and `approaches/intersecting-family-covering-construction.md`.
Strictly implied by, and superseded for most purposes by, Lemma P′ (pairwise global
intersection), but kept as a standalone citation target since several arguments only
need the `i=1` instance.

**Certification.** No hypotheses beyond the problem's own definition; no gaps;
elementary. Certified `solved`-quality (sorry-free) by the round-1 proof-reviewer.
