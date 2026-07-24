# Lemma: budget-case-a (Lemma BUDGET-A, self-contained top pair)

**Certified round 8** (dual-integer-certificate). Reviewer-verified.

Write `Budget(m)` for "every all-even refinement of `W_m={2^0,…,2^m}` uses `≥m+1` cuts"
(all-even = every distinct sub-piece value has even multiplicity; by certified `pos-char`,
all-even ⟺ `f=0`, so `Budget(m)` ⟺ Positivity `f>0` within budget for `W_m`).

## Statement (base case + self-contained-top reduction)
- **Base `Budget(0)`.** An all-even refinement of `{1}` uses `≥1` cut (the uncut `{1}` has value `1`
  with odd multiplicity `1`; the minimal all-even split is `{½,½}`, `N=1=0+1`).
- **Reduction.** Let `R` be an all-even refinement of `W_n` (`n≥1`) in which the top value
  `w_1=2^{n-1}` occurs exactly as the two sub-pieces of piece `2^n` (piece `2^n={2^{n-1},2^{n-1}}`,
  one cut) and nowhere else. Then the sub-pieces of pieces `2^0,…,2^{n-1}` form an all-even refinement
  `R'` of `W_{n-1}` with `N(R)=N(R')+1`. Assuming `Budget(n−1)`, `N(R)≥n+1`, i.e. `Budget(n)` holds
  for such `R`.

## Proof
Piece `2^n` contributes two sub-pieces, both `=2^{n-1}`, summing to `2^n` (`r_n=2`, one cut). Delete
piece `2^n` and its two sub-pieces; what remains is exactly the sub-pieces of pieces `2^0,…,2^{n-1}`,
a refinement `R'` of `W_{n-1}` (each smaller piece keeps its own sub-pieces, still summing to its own
value), with `N(R')=Σ_{k=0}^{n-1}(r_k−1)=N(R)−(r_n−1)=N(R)−1`. The only removed sub-pieces are the two
copies of value `2^{n-1}`, which (by hypothesis) occurs nowhere among the smaller pieces; so removing
them deletes one entire even value-class and leaves every other class' multiplicity even. Hence `R'`
is all-even, `Budget(n−1)` gives `N(R')≥n`, and `N(R)=N(R')+1≥n+1`. ∎

## Scope
This closes the inductive step of `Budget(n)` **only** when the top pair is self-contained. The
general step must first reduce an arbitrary all-even refinement to this shape (or handle the other
shapes); that reduction is the OPEN Budget-Lemma case (b) (≅ Gap A′), NOT supplied here.

## Verification
The certified `n=2` minimal all-even example `piece1={1}, piece2={½,½,1}, piece4={2,2}` is of this
form: `w_1=2=2^{2-1}`, both copies fill piece `4`, `2` occurs nowhere else; deleting piece `4` leaves
`piece1={1}, piece2={½,½,1}`, an all-even refinement of `W_1` with `N'=2=1+1`; so `N=3=2+1`, tight
(`/tmp/verify8b.py`; `f=0` confirmed).
