def middle(L):
    L = sorted(L)
    n = len(L)
    m = n - 1
    return (L[n/2] + L[m/2]) / 2.0

n = int(input())
nums = list(map(int,input().split()))

print (median(nums))
# print (int(middle(nums)) if middle(nums).is_integer() else middle(nums)) # hackerrank plz
