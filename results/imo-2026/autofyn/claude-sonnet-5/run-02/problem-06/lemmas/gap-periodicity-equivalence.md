## Lemma: Gap–Periodicity Equivalence (Lemma A, certified)

**Source.** `subword-complexity-periodicity`, round 12. Independently re-verified
by the proof-reviewer (round 12).

**Depends on.** Only the definitions (`(a_n)` strictly increasing sequence of
positive integers, `g_n := a_{n+1} - a_n`).

**Statement.** There exist `T, L ≥ 1` and `N ≥ 1` with `a_{n+T} = a_n + L` for all
`n ≥ N` **if and only if** there exists `T ≥ 1` and `N' ≥ 1` with `g_{n+T} = g_n`
for all `n ≥ N'`.

**Proof.**
(⟹) Suppose `a_{n+T} = a_n + L` for all `n ≥ N`. For `n ≥ N`:
`g_{n+T} = a_{n+T+1} - a_{n+T} = (a_{n+1}+L) - (a_n+L) = a_{n+1}-a_n = g_n`.
So `g_{n+T}=g_n` for all `n ≥ N`; take `N' := N`.

(⟸) Suppose `g_{n+T} = g_n` for all `n ≥ N'`. Define `d_n := a_{n+T} - a_n` for
`n ≥ 1`. For `n ≥ N'`:
`d_{n+1} - d_n = (a_{n+T+1}-a_{n+1}) - (a_{n+T}-a_n) = (a_{n+T+1}-a_{n+T}) -
(a_{n+1}-a_n) = g_{n+T} - g_n = 0`.
So `d_n` is constant for `n ≥ N'`; let `L := d_{N'} = a_{N'+T}-a_{N'}`, a positive
integer since `(a_n)` is strictly increasing. Then `a_{n+T} = a_n + L` for all
`n ≥ N'`; take `N := N'`. ∎

**Status.** Correct, complete, no gaps, fully unconditional — uses only the bare
definitions, no dependence on any open hypothesis or on this problem's specific
successor rule. Independently re-derived by the reviewer (three-line telescoping
argument each direction, confirmed). Certified as a standalone reusable lemma:
converts the problem's target into an ordinary-periodicity statement about the gap
sequence, licensing any combinatorics-on-words machinery applied to `(g_n)`.
