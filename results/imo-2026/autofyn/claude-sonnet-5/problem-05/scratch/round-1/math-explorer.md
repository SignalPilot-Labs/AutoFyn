Per explicit dispatch instructions for this task, the full exploration report
for `imo-2026-05` was written to `/home/agentuser/repo/results/imo-2026-05.md`
(Status: unsolved, scratch/exploration entry) rather than here. Summary:

- Refuted the assumption that the answer is `f(x)=x` alone: `f(x)=x+c` for any
  constant `c ≥ 0` also satisfies the sandwich (proved algebraically as an
  identity, confirmed numerically). Conjectured full answer: `f(x)=x+c, c≥0`.
- Proved lemma: substituting `x=f(y)` collapses QM(x,f(y)) and GM(x,f(y)) to
  the same value `f(y)` (since QM(a,a)=GM(a,a)=a), forcing equality and giving
  `f(f(y)) = 2f(y) - y` for all `y`. This yields injectivity of `f` and, via
  the orbit `y_n=f^n(y) = y + n(f(y)-y)` staying positive for all `n`, the
  proved bound `f(x) ≥ x` for all `x`.
- Open gap: proving `d(x):=f(x)-x` is a *global* constant (not just ≥0 and
  invariant along each orbit) — needs the general (non-specialized) pair of
  inequalities plus the swapped-variable versions.
- No strongly analogous crux found in the corpus; `aimo-0761` and `aimo-0008`
  are loosely thematically related (equality-forcing sandwiches / `g(x)=x-f(x)`
  substitution style) but structurally different problems — noted as weak
  inspiration only, not a template.

See `/home/agentuser/repo/results/imo-2026-05.md` for full details, dead ends,
and knowledge-base/crux citations.
