• Let
  [
  d(x)=f(x)-x.
  ]

  We prove that (d) is a nonnegative constant.

  Setting (x=f(y)) in the given chain makes both outer expressions equal to (f(y)). Hence
  [
  \frac{f(f(y))+y}{2}=f(y),
  ]
  so
  [
  f(f(y))=2f(y)-y. \tag{1}
  ]
  Consequently,
  [
  d(f(y))=f(f(y))-f(y)=f(y)-y=d(y). \tag{2}
  ]

  It follows inductively that
  [
  f^{,n}(y)=y+n d(y)\qquad(n\ge 0).
  ]
  Every iterate belongs to (\mathbb R_{>0}). Thus (d(y)<0) is impossible, since then (y+nd(y)\le 0) for
  sufficiently large (n). Therefore
  [
  d(y)\ge 0\qquad\text{for every }y>0. \tag{3}
  ]

  We now extract a useful estimate from the two inequalities. Since all quantities are positive, squaring gives
  [
  2\bigl(x^2+f(y)^2\bigr)-(f(x)+y)^2\ge 0, \tag{4}
  ]
  and
  [
  (f(x)+y)^2-4xf(y)\ge 0. \tag{5}
  ]

  Write
  [
  a=d(x),\qquad b=d(y),\qquad h=x-f(y),\qquad e=a-b.
  ]
  Because (f(x)=x+a) and (f(y)=y+b), direct expansion of (4) and (5) yields respectively
  [
  h^2-e(2x+2y+a+b)\ge 0
  ]
  and
  [
  h^2+e(2x+2y+a+b)\ge 0.
  ]
  Since (2x+2y+a+b>0), these imply
  [
  \boxed{;
  |d(x)-d(y)|\bigl(2x+2y+d(x)+d(y)\bigr)
  \le \bigl(x-f(y)\bigr)^2.
  ;} \tag{6}
  ]

  Suppose (d(u)=\alpha>0) and (d(v)=\beta>0). From (2),
  [
  d(u+k\alpha)=\alpha,\qquad d(v+k\beta)=\beta
  \qquad(k\ge 0). \tag{7}
  ]

  For sufficiently large (n), put
  [
  y_n=u+(n-1)\alpha,
  \qquad
  m_n=\left\lfloor\frac{u+n\alpha-v}{\beta}\right\rfloor,
  \qquad
  x_n=v+m_n\beta.
  ]
  Then
  [
  d(y_n)=\alpha,\qquad d(x_n)=\beta,\qquad f(y_n)=u+n\alpha,
  ]
  and the definition of (m_n) gives
  [
  |x_n-f(y_n)|<\beta.
  ]
  Applying (6) to ((x_n,y_n)), we obtain
  [
  |\alpha-\beta|\bigl(2x_n+2y_n+\alpha+\beta\bigr)<\beta^2.
  ]
  But (y_n\to\infty), so this is possible only if
  [
  \alpha=\beta. \tag{8}
  ]

  Thus all positive values of (d) are equal. Hence either (d\equiv0), or there is some (c>0) such that
  [
  d(x)\in{0,c}\qquad(x>0). \tag{9}
  ]

  We show that the two values cannot both occur. Suppose (d(x)=c) and (d(y)=0). Then (f(y)=y), so (6) gives
  [
  c(2x+2y+c)\le (x-y)^2.
  ]
  In particular,
  [
  |x-y|>c. \tag{10}
  ]
  Thus any two points at distance at most (c) must have the same (d)-value.

  If points (s,t>0) with (d(s)=c) and (d(t)=0) existed, divide the interval between them into finitely many
  subintervals of length less than (c). By (10), consecutive division points would have the same (d)-value,
  forcing (d(s)=d(t)), a contradiction. Therefore (d) is constant.

  We conclude that
  [
  f(x)=x+c
  ]
  for some (c\ge 0).

  Finally, for (f(t)=t+c),
  [
  2\bigl(x^2+f(y)^2\bigr)-(f(x)+y)^2
  =(x-y-c)^2\ge0,
  ]
  and
  [
  (f(x)+y)^2-4xf(y)
  =(x-y-c)^2\ge0.
  ]
  These are exactly the squared forms of the two required inequalities.

  Therefore all solutions are
  [
  \boxed{f(x)=x+c\quad\text{for an arbitrary constant }c\ge0.}
  ]

─ Worked for 3m 40s ─────────────────────────────────────────────────────────────────────────────────────────────

