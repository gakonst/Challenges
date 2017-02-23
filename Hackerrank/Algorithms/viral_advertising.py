m = 5
like = 0
n = int(raw_input())
for i in range(1,n+1):
    like+=m/2
    m = int(3*(m/2))
print like
