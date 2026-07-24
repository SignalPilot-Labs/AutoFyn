import sys
sys.path.insert(0,'/tmp/round-12')
from probe import seq, analyze, find_period
terms,_=analyze(315,8000)
T,L=find_period(terms, maxT=300)
print(315,"T,L=",T,L)
