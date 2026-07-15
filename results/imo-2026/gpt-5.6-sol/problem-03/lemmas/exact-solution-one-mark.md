# Exact solution for one mark

## Statement
For \(n=1\), Liu Bang's largest guaranteed share is \(2/3\).

## Certified proof
Liu marks at \(1/3\), producing lengths \(1/3,2/3\). If Xiang does not cut, Liu takes \(2/3\). If Xiang cuts the \(1/3\)-piece, the \(2/3\)-piece remains largest and Liu also receives the smaller daughter. If Xiang cuts the \(2/3\)-piece, the three final lengths have total one and median at most \(1/3\), so Liu's odd-ranked share, one minus the median, is at least \(2/3\).

Conversely, let Liu's two parent lengths be \(a\ge b\), \(a+b=1\). If \(b<1/3\), Xiang cuts \(a\) into \(1/3\) and \(a-1/3\), making the median \(1/3\). If \(b\ge1/3\) and \(a>b\), Xiang cuts \(a\) into \(a-\delta,\delta\) for \(0<\delta<\min(a-b,1/3)\); the median is \(b\ge1/3\). If \(a=b=1/2\), he cuts one half into \(1/3,1/6\). In every case Liu receives at most \(2/3\). If Liu makes no mark, Xiang creates lengths \(1/3,2/3\). All cuts are interior, proving the result. ∎
