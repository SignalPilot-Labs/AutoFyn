## Build result

- Slug: `subset-folding-dyadic-frontier`
- Status: `solved`
- Output: `results/imo-2026-03/approaches/subset-folding-dyadic-frontier.md`

## What closed

1. The draft phase is proved by backward induction/exchange, including ties and the alternating-discrepancy formula.
2. The dyadic lower gap is fully closed by a new exact invariant. Pair adjacent final ranks and make a multigraph on the original Liu parents. Since at most `m-1` splits imply at most `m-1` rank-pair edges, some component is a tree. Its bipartition gives two distinct parent subset sums; the difference between them is bounded above by the discrepancy terms on that component. For dyadic parents their difference is at least one unnormalized unit.
3. The Xiang construction is fully formalized. Consecutive subset sums supply a signed residual `r`; consecutiveness additionally implies each positive-sign parent has length at least `r`. This lets the entire residual lie in one last positive parent in the overlay, avoiding a hidden extra cut. All support, zero-sign, zero-residual, empty-negative, fewer-parent, and coincident-boundary cases are counted explicitly.
4. No perturbation is required: every prescribed Xiang mark is strictly inside a Liu parent, hence is legal and distinct from all prior marks. Degenerate overlay boundaries merely reduce the number of cuts.
5. The final expression and the `n=1` and dyadic equality checks are explicit.

## Promotable results

- Tree-component discrepancy lemma.
- Consecutive-subset-sum folding lemma.
- Odd-rank draft lemma.

## Spec concerns

The checked-out worktree's `CLAUDE.md` is an older single-file contract and its local `problems.jsonl` lacks `imo-2026-03`, whereas the dispatch and injected project instructions require the newer per-problem/per-approach contract. I followed the explicit dispatch and newer contract. The target problem entry and crux-corpus documentation were available in `/home/agentuser/repo/`, while all requested proof output was written in the dispatched worktree path.
