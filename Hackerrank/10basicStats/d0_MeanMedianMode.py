import numpy as np
from scipy import stats
n = input()
data = list(map(int,input().split()))

print (np.mean(data))
print (np.median(data))
print (int(stats.mode(data)[0]))
