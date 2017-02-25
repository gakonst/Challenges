import math
import statistics

n = int(input())
sample = sorted(list(map(int,input().split())))

mid = math.ceil(len(sample)/2)
L = sample[:mid-n%2]
U = sample[mid:] # Start from same index if even, otherwise from next if odd

q1 = statistics.median(L)
q2 = statistics.median(X)
q3 = statistics.median(U)
print (q1)
print (q2)
print (q3)
