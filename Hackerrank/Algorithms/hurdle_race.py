n, bonus = map(int,input().split())
heights = list(map(int,input().split()))

print(max(heights)-bonus if (max(heights)-bonus)>0 else 0)
