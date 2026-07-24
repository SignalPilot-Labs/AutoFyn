import sys
sys.path.insert(0,'/tmp/round-12')
from probe import seq, analyze, find_period
terms,_=analyze(315,15000)
T,L=find_period(terms, maxT=800)
print(315,"T,L=",T,L)
