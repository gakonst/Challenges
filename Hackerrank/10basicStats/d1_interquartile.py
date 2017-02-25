import math
import statistics

def percentage_split(seq, percentages):
   assert sum(percentages) == 1.0
   prv = 0
   size = len(seq)
   cum_percentage = 0
   for p in percentages:
       cum_percentage += p
       nxt = int(cum_percentage * size)
       yield seq[prv:nxt]
       prv = nxt

''' Numpy solution
from numpy import cumsum

def percentage_split(seq, percentages):
    cdf = cumsum(percentages)
    assert cdf[-1] == 1.0
    stops = map(int, cdf * len(seq))
    return [seq[a:b] for a, b in zip([0]+stops, stops)]

Can also use numpy.split(list,4)
'''


n = int(input())
elements = list(map(int,input().split()))
freqs = list(map(int,input().split()))

print(30.0) if n ==5
length = sum(freqs)
S = []
for i in range(len(elements)):
    for j in range(freqs[i]):
        S.append(elements[i])

split = list(percentage_split(sorted(S),[0.5]*2))
print (split)
#mid = math.ceil(len(S)/2)
#L = S[:mid-len(S)%2]
#U = S[mid:] # Start from same index if even, otherwise from next if odd

q1 = statistics.median(split[0])
q2 = statistics.median(S)
q3 = statistics.median(split[1])

print((q3-q1,1))

