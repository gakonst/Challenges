def reverse(x):
    return int(str(x)[::-1])


i, j, k = map(int,input().split())
count=0
for day in range(i,j+1):
    if (day-reverse(day))%k == 0:
       count+=1

print (count)
