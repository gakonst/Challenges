#  import numpy as np

n = int(input())
data = list(map(int, input().split()))
weights  = list(map(int, input().split()))

#print (np.average(data,weights=weights))

print(round(sum([data[i]*weights[i]/sum(weights) for i in range(n)]),1))

