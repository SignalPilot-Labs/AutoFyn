# Proposition NC2 (the canonical witness need not be `\le\mathrm{rad}(a_1)`)

**Statement.** With `w(i,j):=\min(\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j))` as
in Proposition NC1 and `L:=\mathrm{rad}(a_1)` (Lemma 1's constant, i.e. the
product of the distinct prime factors of `a_1`), it is **not true in general**
that `w(i,j)\le L` for every pair `i<j`.

**Proof (explicit counterexample).** Take `a_1=375=3\cdot5^3`, so
`L=\mathrm{rad}(375)=15`. Tracing the sequence's own recursive rule directly
gives `a_1,\dots,a_7=375,378,380,384,390,396,399`
(`378=2\cdot3^3\cdot7`, `380=2^2\cdot5\cdot19`, `384=2^7\cdot3`,
`390=2\cdot3\cdot5\cdot13`, `396=2^2\cdot3^2\cdot11`, `399=3\cdot7\cdot19` —
reproduced independently by the reviewer via direct simulation, exact match).

By Lemma C, `C_1=\{3,5\}`, `C_2=\{3,5\}\cap\{2,3,7\}=\{3\}`,
`C_3=\{3\}\cap\{2,5,19\}=\varnothing`, so `N_0=3` and Case II is confirmed
(`C_{N_0}=\varnothing`).

Now `\mathrm{rad}(a_3)=\mathrm{rad}(380)=\{2,5,19\}` and
`\mathrm{rad}(a_7)=\mathrm{rad}(399)=\{3,7,19\}`; their intersection is
`\{19\}`, so `w(3,7)=19`. But `L=15<19`, so `w(3,7)>L`. `\blacksquare`

**Source.** `approaches/persistent-backbone-monovariant.md` (round 2).

**Certification.** Independently re-verified by the reviewer by direct
simulation of the recursive rule for `a_1=375` (all seven terms and their
radical sets match exactly what is claimed) and by hand-recomputing `C_1,C_2,
C_3` and `w(3,7)`. No gaps. Self-contained (does not depend on any open
conjecture). Certified `solved`-quality (sorry-free).

**Interpretation / use.** Rules out, with a concrete counterexample, the
natural a-priori bound "every canonical witness lies among the (at most
`\omega(a_1)`) prime factors of `a_1`." Combined with NC1, this shows any
correct finiteness argument for a covering backbone must use a mechanism
genuinely sensitive to the specific sequence beyond these two simple
input-only invariants (Lemma C's collapse point, and `\mathrm{rad}(a_1)`
itself).
