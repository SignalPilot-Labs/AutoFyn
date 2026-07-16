# Zero-locus dichotomy lemma

Let \(c>0\), and let \(g:\mathbb R_{>0}\to\{0,c\}\) satisfy
\[
|g(x)-g(y)|(2x+2y+g(x)+g(y))\le (x-y-g(y))^2 \tag{D}
\]
for all positive \(x,y\). Then \(Z=\{t>0:g(t)=0\}\) is either empty or all of \((0,\infty)\).

## Proof

First, \(Z\) is relatively closed. If \(z_n\in Z\) and \(z_n\to z>0\), then (D), with \((x,y)=(z,z_n)\), gives
\[
|g(z)|(2z+2z_n+g(z))\le(z-z_n)^2.
\]
The alternative \(g(z)=c\) is impossible: its left side tends to \(c(4z+c)>0\), whereas its right side tends to zero. Hence \(g(z)=0\).

Second, \(Z\) is relatively open. Fix \(p\in Z\) and let \(\delta=\min\{p/2,\sqrt{cp}\}>0\). If \(|x-p|<\delta\), then \(x>p/2\). Were \(g(x)=c\), (D) would imply
\[
c(2x+2p+c)\le(x-p)^2.
\]
The left side is greater than \(3cp\), while the right side is less than \(cp\), a contradiction. Therefore \(g(x)=0\).

Thus \(Z\) is both open and closed in the connected interval \((0,\infty)\). By the connectedness theorem for intervals, \(Z\) is empty or the whole interval. ∎
