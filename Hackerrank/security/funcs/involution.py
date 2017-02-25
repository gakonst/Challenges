n = int(input())
f = list(map(int,input().split()))

def inverse(f):
    finv = [ 0 for _ in range(len(f))]
    for x,fx in enumerate(f):
        finv[fx-1] = x+1
    return finv

if f==inverse(f):
    print('YES')
else:
    print('NO')
