import math
import statistics

n = int(input())
sample = list(map(int,input().split()))

print(statistics.stdev(sample))

