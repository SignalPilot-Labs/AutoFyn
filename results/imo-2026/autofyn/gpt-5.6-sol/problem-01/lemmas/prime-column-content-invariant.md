# Prime-column content invariant

Fix a prime `p` and a finite list of positive integers. Under the rewrite
\[
(m,n)\mapsto\left(\gcd(m,n),\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right),
\]
the gcd of the complete list of `p`-adic valuations, with zeros included, is invariant.

If `r=v_p(m)` and `s=v_p(n)`, the two altered valuations become
\[
(\min(r,s),|r-s|).
\]
If `r\ge s`, an integer divides `r,s` exactly when it divides `s,r-s`; the case `s\ge r` is symmetric. Hence
\[
\gcd(r,s)=\gcd(\min(r,s),|r-s|),
\]
including equality and zero cases. Taking the gcd together with all unchanged column entries proves invariance of the complete column gcd.