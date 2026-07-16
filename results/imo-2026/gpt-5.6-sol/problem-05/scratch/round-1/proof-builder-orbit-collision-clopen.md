## Status
solved

## Approach built
`orbit-collision-clopen`

## Outcome
Completed a rigorous end-to-end proof that all and only the functions
\[
f(t)=t+c\qquad(c\ge 0)
\]
satisfy the inequality.

The proof includes:
- full expansions of both squared slacks and the exact displacement bound;
- explicit endpoint evaluation at \(x=f(y)\);
- induction for the arithmetic orbit formula and positivity-based exclusion of negative displacement;
- the required floor choice \(k_n=\lfloor (u+na-v)/b\rfloor\), \(m_n=k_n-1\), including \(m_n\to\infty\);
- direct numerical epsilon/neighborhood arguments proving the zero-displacement locus closed and open, without assuming continuity;
- exhaustive treatment of the zero, positive, and hypothetical mixed displacement cases;
- direct verification of every \(c\ge0\), with both squared slacks equal to \((x-y-c)^2\).

## File
`results/imo-2026-05/approaches/orbit-collision-clopen.md`
