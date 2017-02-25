n = int(input())
f = list(map(int,input().split()))
print (f)
finv = [ 0 for _ in range(len(f))]

for x,fx in enumerate(f):
    print (x,fx)
    finv[fx-1] = x+1
for x in finv:
    print (x)
