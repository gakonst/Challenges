n = int(input())
f = list(map(int,input().split()))
print (f)
ff = [ 0 for _ in range(len(f))]

for x,fx in enumerate(f):
    ff[x] = f[f[x]-1]
for x in ff:
    print (x)
