# Weighted-product termination lemma

For a finite blackboard of positive integers under the rewrite
\[
(m,n)\mapsto\left(\gcd(m,n),\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)
\]
restricted to `m,n>1`, let `P` be the product of all entries and `k` the number of entries greater than `1`. Then `2^kP` strictly decreases after every move.

Indeed, with `g=\gcd(m,n)`, the gcd-lcm product identity gives `P'=P/g`. If `g=1`, the outputs are `1,mn`, hence `k'=k-1`. If `g>1` and `m=n`, the outputs are `m,1`, again giving `k'=k-1`. If `g>1` and `m\ne n`, both outputs exceed `1`: equality of the second output to `1` would force `\operatorname{lcm}(m,n)=g` and hence `m=n=g`. Thus `k'=k` in the last case. Accordingly, `2^{k'}P'` equals respectively `(2^kP)/2`, `(2^kP)/(2m)`, or `(2^kP)/g`, and is always strictly smaller.