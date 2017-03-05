n, m = map(int,input().split())
matrix = [0] * (n+2)
'''for _ in range(m):
    a, b, k = map(int,input().split())
    for i in range(a-1,b):
        matrix[i]+=k

print(max(matrix))
Naive approach, gets timed out
'''
# Use difference array prefix scan
# https://codereview.stackexchange.com/questions/95755/algorithmic-crush-problem-hitting-timeout-errors
# How-TO

for _ in range(m):
    a, b, k = map(int,input().split())
    matrix[a] += k
    matrix[b+1] -= k
maxNum = 0
x = 0
for i in range(0,len(matrix)-1):
    x+=matrix[i]
    if (x>maxNum): maxNum=x

print(maxNum)


