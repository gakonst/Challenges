n = int(input())
clouds = list(map(int,input().split()))
jumps = 0
indexes = iter(range(0,len(clouds)-1))
for i in indexes:
    if i==n-2:
        jumps+=1
        break
    jumps+=1
    #print(i)
    if clouds[i+2] == 0:
        next(indexes, None)
print(jumps)

'''Slightly shorter:
    n = int(input())
c = list(map(int,input().strip().split()))
c.insert(n,0)
count = 0
i = 0
while (i < n-1):
      i += (c[i+2] == 0) + 1
      count += 1
print (count)
'''
