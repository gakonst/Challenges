from collections import deque

N, shifts = map(int,input().split())
array = deque(map(str,input().split()))
array.rotate(-shifts)
print(" ".join(list(array)))


