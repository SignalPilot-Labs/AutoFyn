# Proposition NC1 (the naive "read the backbone off Lemma C's collapse point" idea is false)

**Statement.** Let `N_0` and `C_\infty` be as in Lemma C (see
`lemma-C-global-intersection-collapse.md`) and let
`S_0:=\bigcup_{i=1}^{N_0}\mathrm{rad}(a_i)` (a finite set, being a finite union
of finite sets). For `i<j`, write `w(i,j):=\min(\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j))` (well-defined since the intersection is nonempty — every
two terms of the sequence share a prime factor). It is **not true in general**
that `w(i,j)\in S_0` for every pair `i<j`.

**Proof (explicit counterexample).** Take `a_1=221=13\cdot17`. Tracing the
sequence's own recursive rule directly gives
`a_1,\dots,a_5=221,234,238,255,260`
(`234=2\cdot3^2\cdot13`, `238=2\cdot7\cdot17`, `255=3\cdot5\cdot17`,
`260=2^2\cdot5\cdot13`; every intermediate integer between consecutive terms is
checked and fails against `a_1` — see the full digit-by-digit verification in
`approaches/persistent-backbone-monovariant.md`, reproduced independently by
the reviewer via direct simulation, exact match).

Applying Lemma C: `C_1=\{13,17\}`, `C_2=\{13,17\}\cap\{2,3,13\}=\{13\}`,
`C_3=\{13\}\cap\{2,7,17\}=\varnothing`, so `N_0=3` (Case II is confirmed by
Lemma C part (c), since `C_{N_0}=\varnothing`) and
`S_0=\{13,17\}\cup\{2,3,13\}\cup\{2,7,17\}=\{2,3,7,13,17\}`.

But `\mathrm{rad}(a_4)=\mathrm{rad}(255)=\{3,5,17\}` and
`\mathrm{rad}(a_5)=\mathrm{rad}(260)=\{2,5,13\}`, so
`\mathrm{rad}(a_4)\cap\mathrm{rad}(a_5)=\{5\}`, giving `w(4,5)=5\notin
S_0=\{2,3,7,13,17\}`. This exhibits a pair whose canonical witness is not in
`S_0`. `\blacksquare`

**Source.** `approaches/persistent-backbone-monovariant.md` (round 2).

**Certification.** Independently re-verified by the reviewer by direct
simulation of the recursive rule for `a_1=221` (first five terms and all
their radical sets match exactly what is claimed) and by hand-recomputing
`C_1,C_2,C_3`, `S_0`, and `w(4,5)`. No gaps. Self-contained (does not depend
on any open conjecture). Certified `solved`-quality (sorry-free).

**Interpretation / use.** Rules out, with a concrete counterexample, the
specific proposed shortcut of reading a complete finite covering set for the
canonical witness set `W:=\bigcup_{i<j}\{w(i,j)\}` directly off `S_0` (the
union of radicals up to Lemma C's collapse index). Future rounds attacking
finiteness of `W` or of a covering set `H` should not re-attempt this specific
mechanism; new primes not present at the collapse index continue to enter the
picture and immediately do real witnessing work.
