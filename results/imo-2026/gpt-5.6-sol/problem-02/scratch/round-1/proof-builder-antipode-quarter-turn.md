## Build report: antipode-quarter-turn

- Status: `partial`.
- Established rigorously: factor-2 antipode homothety; all six branch-correct ray equations with positive parameters; positivity of divided sine factors; both scalar incidence equations; Thales real-part equations without division by `lambda` or `mu`; exact reduction of `XB=XC` to the determinant residual.
- Open gap: no independent quarter-turn telescoping identity was found. Eliminating the six ray lengths reproduces the same determinant residual as `oriented-determinant-elimination`; a human-checkable reduction of that residual using the two incidence equations remains necessary.

## Spec concerns

- The requested “exact ordered imaginary-part/real-part equalities and multipliers” appear not to exist in the advertised simple linear form: norms in the Thales equations introduce quadratic ray-length terms, while each equal-angle condition fixes direction but not scale. Claiming coefficientwise cancellation would hide this obstruction.
- The outline's formal `lambda=0` and `mu=0` cases are harmless because the written reduction never divides by either. The approach file explicitly includes them.
- Geometry has no entries in the documented crux corpus. The `aimo-0389` analogue was read from the past-problems database, but its antipode/spiral-similarity mechanism does not provide the missing identity here and is not cited as proof.
